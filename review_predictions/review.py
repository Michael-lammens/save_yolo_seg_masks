import os
import shutil
import threading
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Directories
root_dir = ""
main_dir = "predictions/"
approved_dir = "approved/"
rejected_dir = "rejected/"

# Create directories if they don't exist
os.makedirs(approved_dir, exist_ok=True)
os.makedirs(rejected_dir, exist_ok=True)


buffer = [] # Buffer to hold dict of images w/ dynamic paths 
current_index = 0
visited_images = [] # file names of visited path insensitive


def draw_text(text, color, img):
    """Apply a text box on img with color=color and text=text
    Return img with text overlay"""
    draw = ImageDraw.Draw(img)
    font_size = 50
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    # Position | Size
    box_position = (20, 20)  # Top left
    box_size = (text_width + 40, text_height + 20)

    draw.rectangle(
        [box_position, (box_position[0] + box_size[0], box_position[1] + box_size[1])],
        fill=color
    )
    text_position = (box_position[0] + 20, box_position[1] + 10)
    draw.text(text_position, text, fill="white", font=font)
    return img


def load_images():
    """Load images from predictions directory into the buffer"""
    for filename in os.listdir(root_dir + main_dir):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            if filename not in visited_images:
                buffer.append({"file": filename, "parent": main_dir})
                visited_images.append(filename)
                if len(buffer) - current_index >= 5:
                    break

def move_image(destination_dir):
    """Move the current image to the specified directory and update the buffer."""
    global current_index
    if buffer:
        current_image_name = buffer[current_index]["file"]  # name.jpg
        current_image_parent = buffer[current_index]["parent"]  # predictions / approved / rejected
        current_image_path = os.path.join(root_dir, current_image_parent, current_image_name)

        try:
            shutil.move(current_image_path, os.path.join(destination_dir, os.path.basename(current_image_path)))
            buffer[current_index]["parent"] = destination_dir
            current_index += 1
            load_images()
            display_image()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            load_images()  # Reload buffer if there's an error
            display_image()
    else:
        print("Buffer is empty. No image to move.")


def display_image():
    """Display the current image from the buffer in the GUI."""
    if buffer:
        current_image_name = buffer[current_index]["file"]  # name.jpg
        current_image_parent = buffer[current_index]["parent"]  # predictions / approved / rejected
        current_image_path = os.path.join(root_dir, current_image_parent, current_image_name)
        try:
            img = Image.open(current_image_path)
            img = img.resize((740, 740), Image.Resampling.LANCZOS)
            if current_image_parent == "rejected/":
                img = draw_text("REJECTED", "red", img)
            elif current_image_parent == "approved/":
                img = draw_text("APPROVED", "green", img)
            else:
                img = draw_text("UNASSIGNED", "purple", img)
            img_tk = ImageTk.PhotoImage(img)
            panel.config(image=img_tk)
            panel.image = img_tk
        except FileNotFoundError as e:
            print(f"Error: {e}")
            buffer.pop(current_index)  # Remove the missing file from the buffer
            load_images()  # Reload buffer if there's an error
            display_image()
    else:
        panel.config(image='')
        panel.image = None


def on_key_press(event):
    """Handle key press events."""
    if event.keysym == "space":
        move_image(approved_dir)
    elif event.keysym == "m":
        move_image(rejected_dir)
    elif event.keysym == "Right":
        next_image()
    elif event.keysym == "Left":
        previous_image()


def next_image():
    """Display the next image in the buffer."""
    global current_index
    if buffer and current_index < len(buffer) - 1:
        current_index += 1
        load_images()
        display_image()


def previous_image():
    """Display the previous image in the buffer."""
    global current_index
    if buffer and current_index > 0:
        current_index -= 1
        load_images()
        display_image()

# Create the main window
root = tk.Tk()
root.title("Image Approval")

# Create and place image display
panel = tk.Label(root)
panel.pack()

# Create and place buttons
red_button = tk.Button(root, text="Bad", bg="red", fg="black", command=lambda: move_image(rejected_dir))
red_button.pack(side="left", padx=20, pady=20)

green_button = tk.Button(root, text="Good", bg="green", fg="black", command=lambda: move_image(approved_dir))
green_button.pack(side="right", padx=20, pady=20)

# Bind keys to the respective functions
root.bind("<space>", on_key_press)
root.bind("m", on_key_press)
root.bind("<Right>", on_key_press)
root.bind("<Left>", on_key_press)

# Load initial set of images and display the first
load_images()
display_image()

root.mainloop()
