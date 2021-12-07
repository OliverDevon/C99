import os, shutil
import os, shutil
source = input('Enter source of the file: ')
destination = input('input the destination of the file: ')
source=source+'/'
destination=destination+'/'
for file in os.listdir(source):
    shutil.copy(source, destination)