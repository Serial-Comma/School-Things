# fileOperations.py
# Version: 17_1.01  Date: 02-August-2022 Programmer: Fong KK
## ********* File operations **********
import os
#Constants for file status
FILE_NOTFOUND = 0
FILE_EMPTY    = 1
FILE_EXIST    = 2
def FileChecking(sourceFile):
     fileStatus = FILE_NOTFOUND
     if os.path.exists(sourceFile):
          EmployeeFile = open(sourceFile,"r")
          print(f"\n\t ****** File {sourceFile} was found ******")
          if os.path.getsize(sourceFile) == 0:
               print(f"\n\t ****** File {sourceFile} is empty  ******")
               fileStatus = FILE_EMPTY
          else:# File is not empty, can read or append records or overwite file
               # EmployeeFile = open(sourceFile, "r") # or 'a', 'w'
               fileStatus = FILE_EXIST
          EmployeeFile.close     
     else:
          print(f"\n\t ****** File {sourceFile} not found *******")
          #EmployeeFile = open(sourceFile, "w") #open new file
          fileStatus = FILE_NOTFOUND
     return fileStatus
