import zipfile
import os

path_to_zip_files = 'C:\\Users\\ndukw\Desktop\Data analysis capstone\path 1'
directory_to_extract_to = "C:\\Users\\ndukw\Desktop\Data analysis capstone\path 1\extracted"

os.chdir(path_to_zip_files)
def multi_unzipper(path_to_zip_files, directory_to_extract_to):
    try:
        os.makedirs(directory_to_extract_to)
        os.mkdir(directory_to_extract_to)
        print('Folder created')
    except FileExistsError:
        print('Folder already exists')

    for entry in os.listdir(path_to_zip_files):
        if not entry.startswith('.') and entry.endswith(".zip"):
            # open zip file
            print(entry)
            file_name = os.path.abspath(entry)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(directory_to_extract_to)
            zip_ref.close()
            print('extracted!')
    print('Done!')


multi_unzipper(path_to_zip_files, directory_to_extract_to)
