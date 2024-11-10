# importing os module 
import os

def list_directory_contents(directory_path):
    # list down the contents of the directory
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
# path of the directory
directory_path = "./"
list_directory_contents(directory_path)
