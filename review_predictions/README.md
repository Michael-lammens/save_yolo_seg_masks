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

Buffer will always hold dictionary of path sections of the images visited + the next 5 in predictions/
- Can use a script to get all image names from approved/ and copy the respective .txt files from masks/ to actually use the mask files from approved.
## Todo
- Instead of moving the actual images just use a csv/txt for of the file names prepended with mask/. Not sure why didnt start with this
- Add option to show the images with their mask from masks/ for when the input images dont have masks already applied

## Ideas
- Add ability to hover masks which will change the display to highlight the mask hovered
- Using the mask + original image, add ability to click specific labels and customize the polygon
- Could even add a similar "smart polygon" feature like the one used in rboflow
  - If active, click on a bounded box to run inference on the section within the bounded box. From the output apply the resulted mask over the image OR
    add the label-coordinates to the active mask file. 
- Add a configuration step to use your own labels / colors and ability to customize encodings of the output masks
- Delete / add polygons with changes reflected in the label file



