import os 
import shutil

source = input("Enter your source folder name:")
destination = input("Enter your destination:")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source + file),destination)