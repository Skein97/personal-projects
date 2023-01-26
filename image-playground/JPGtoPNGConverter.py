import sys
import os
from PIL import Image

# Grab first (folder to be converted) and second argument (new folder to store converted images)
input_folder = sys.argv[1]
output_folder = sys.argv[2]


def image_converter(input_folder, output_folder):
    # Check if new folder exist if not create
    try:
        os.mkdir(output_folder)
        print('Folder created')
    except FileExistsError:
        print('Folder already exists')

    # Loop through input folder
    for entry in os.scandir(input_folder):
        if not entry.name.startswith('.') and entry.is_file():
            # Create a new name for the file
            old_name = entry.name
            (name, file_type) = old_name.split('.')
            new_name = name + '.' + 'png'
            # open the image
            img = Image.open(input_folder + '/' + old_name)
            # Convert images to png
            img.save(output_folder + '/' + new_name, 'png')
            print(f'{name} converted and saved!')

    print('All done!')


image_converter(input_folder, output_folder)

# convert the images to png,
# then save them to new folder
