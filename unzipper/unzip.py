import zipfile

path_to_zip_file = input('Path to zip file: ')
directory_to_extract_to = input('Directory to extract to: ')

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

print('Done!')