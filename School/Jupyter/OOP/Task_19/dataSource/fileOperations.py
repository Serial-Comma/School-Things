##fileOperations.py
#Date 17 Aug 2022
## Check the status of file
import os
#constant for file status
FILE_NOTFOUND=0
FILE_EMPTY=1
FILE_EXIST=2

def FileChecking(source):
    fileStatus=FILE_NOTFOUND
    if os.path exists(source):
        with open(source,'r') as f:
            print (f'\n\t *** File {source} was found ***')
            
            if os.path.getsize(source)==0: #file empty
                print (f'File {source} is empty')
                fileStatus=FILE_EMPTY

            else: #File not empty, size>0
                fileStatus=FILE_EXIST
    else:
        print (f'\n\t *** File {source} not found ***')
        fileStatus=FILE_NOTFOUND
    return fileStatus
                
