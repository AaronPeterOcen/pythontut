from PIL import Image
import sys
import os

# image converter to convert images to png and put them in a new folder
# grab the first and second argument
image_folder = sys.argv[1]
out_folder = sys.argv[2]

# check if new exists if not create it
if not os.path.exists(out_folder):
    os.makedirs(out_folder)
# loop through pokedex and convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # splitting text for us
    cleanname = os.path.splitext(filename)[0]
    print(cleanname)
    img.save(f'{out_folder}{cleanname}.png', 'png')
    print('Done')
# save them to new folder
