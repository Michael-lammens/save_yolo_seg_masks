Input/Inferenced images are 640x640 and upsample=True, otherwise must scale the masks. I havent played with non 640x640 images or tested it but will get around to it eventually

## How It Works:
1. Add --save-masks to segment/predict.py argument
2. During inference, only the masks without the bounded boxes are saved to masks/ in the format of <label> <polygon-coordinates> in a .txt file named as the input image.
  - Polygon coordinates are normalized to image size and saved as their contour coordinates


## To review the masks
in review_predictions/ I made a GUI to visualize and buffer the images in the root directory with their bounded boxes and masks from the original predict.py output
I was too lazy to use the masks from masks/ but will add these + other features eventually
For info on the review_predictions usages I added a readme in there

