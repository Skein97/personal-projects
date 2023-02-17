import sys
import os
from PIL import Image

def image_converter(input_folder, output_folder):
    # Check if new folder exist if not create
    try:
        os.makedirs(output_folder)
        os.mkdir(output_folder)
        print('Folder created')
    except FileExistsError:
        print('Folder already exists')

    # Loop through input folder
    for entry in os.listdir(input_folder):
        if not entry.startswith('.') and entry.endswith('heic'):
            # Create a new name for the file
            old_name = entry
            name = old_name.split('.')[0]
            # open the image
            img = Image.open(f'{input_folder}/{old_name}')
            # Convert images to png
            img.save(f'{output_folder}/{name}.jpg', 'jpg')

    print('All done!')


image_converter(sys.argv[1], sys.argv[2])