from openpyxl import Workbook
import csv
import os

path_to_csv_files = "C:\\Users\\ndukw\Desktop\Data analysis capstone\path 1\extracted"
directory_to_save_to = "C:\\Users\\ndukw\Desktop\Data analysis capstone\path 1"

os.chdir(path_to_csv_files)


def csv_to_xlsx_converter_1to1(path_to_csv_files, directory_to_save_to):
    # converts all the individual csv files in the folder to individual xlsx files
    try:
        # try to make the folder to save to
        os.makedirs(directory_to_save_to)
        os.mkdir(directory_to_save_to)
        print('Folder created')
    except FileExistsError:
        # if folder already exists
        print('Folder already exists')

    for file in os.listdir(path_to_csv_files):
        # check for hidden and csv files
        if not file.startswith('.') and file.endswith(".csv"):
            wb = Workbook()  # create new workbook #
            ws = wb.active  # activate workbook #
            name = file.split('.')[0] + '.' + 'xlsx'
            print(f'{file} started!')
            print()
            file_name = os.path.abspath(file)
            with open(file_name, 'r') as f:
                for row in csv.reader(f):
                    ws.append(row)
            wb.save(f'{directory_to_save_to}/{name}')
            print(f'{name} done!')
    print('Done!')


def csv_to_xlsx_converter_all_to_1(path_to_csv_files, directory_to_save_to):
    # converts all the individual csv files in the folder into one xlsx files
    try:
        os.makedirs(directory_to_save_to)
        os.mkdir(directory_to_save_to)
        print('Folder created')
    except FileExistsError:
        print('Folder already exists')

    wb = Workbook()
    ws = wb.active
    new_name = input('New joint file name: ')
    for file in os.listdir(path_to_csv_files):
        if not file.startswith('.') and file.endswith(".csv"):
            print(f'{file} started!')
            file_name = os.path.abspath(file)
            with open(file_name, 'r') as f:
                for row in csv.reader(f):
                    ws.append(row)
            print(f'{file} done!')
    wb.save(f'{directory_to_save_to}/{new_name}')
    print('Done!')


# csv_to_xlsx_converter_1to1(path_to_csv_files, directory_to_save_to)
csv_to_xlsx_converter_all_to_1(path_to_csv_files, directory_to_save_to)
