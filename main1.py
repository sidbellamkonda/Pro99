import os
import shutil
import time

def main():

    sec = time.time()-(30*24*60*60)

    path = '/Users/madhuripanja/Desktop/testFolder2/'

    deletedFolderCount = 0
    deletedFileCount = 0

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if sec >= get_file_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount+=1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if sec >=get_file_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolderCount+=1
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if sec >= get_file_folder_age(file_path):
                        remove_file(file_path)
                        deletedFileCount+=1
    else:
        print("Path not found")
    print("Total number of folders deleted: ")
    print(deletedFolderCount)
    print("Total number of files deleted: ")
    print(deletedFileCount)

def remove_folder(path):
    if not shutil.rmtree(path):
        print("The folder has been removed successfully")
    else:
        print("Unable to delete the folder")
def remove_file(path):
    if not os.remove(path):
        print("The files have been removed successfully")
    else:
        print("Unable to delete the files")

def get_file_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()