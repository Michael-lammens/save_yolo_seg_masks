GUI to manually review output predictions of predict.py, adding them to an approved or rejected directory based on input. 
This is a side project started while trying to speed up mask annotations with model assistance. There's probably services for this already but I wanted to integrate something directly into my yolo workspace and it works well for my usecases, maybe it could work for others too.


## Examples
![Untitled design (4)](https://github.com/user-attachments/assets/8227915d-28c7-42aa-8cc7-4154e1fb0ef0)


## How it works:
1. Using the modified predict.py I run predictions on a full image set with --save-masks
2. I set the input directory of review.py to be the root of the created directory from predict.py
3. Run the script
4. From the masked/bbox prediction images if the masks are good press space bar to add them to approved/ or "m" for rejected/
5. Use arrow keys "<" and ">" to go backwards or forwards without changing assigned status. Can revisist images and change status which will move the location og the image

Buffer will always hold the images visited + the next 5

- Can use a script to get all image names from approved/ and copy the respective .txt files from masks/ to actually use the mask files from approved

## Goals
- Add ability to hover masks and change the display to highlight the mask hovered
- Use the actual images used in inference and apply the mask from masks/, instead of moving the output image move the mask .txt file
- Using the mask + original image, add ability to click specific mask and customize the polygon
- Add a configuration step to use your own labels / colors
- Delete / add polygons



