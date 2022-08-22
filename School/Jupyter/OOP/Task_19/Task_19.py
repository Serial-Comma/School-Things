## Task_19.py
#$ Version: 19.01  Date: 4-August-2022 Programmer: Fong KK
## ***** Module: Composition - Object of class deptAH containing
## AccountHolder and AHDeptHeader objects  *****
import os
import csv
from dataSource.fileOperations import *
from dataSource.deptHeaderClass import AHDeptHeader
from dataSource.AccountHolderClass import AccountHolder
from dataSource.deptAHClass import deptAH

def main():
     CompanyDeptFileName = "dataSource/CompanyDepts.csv" #write to this file
     CompanyDeptCsvFile = open(CompanyDeptFileName, 'w', newline='', encoding='UTF8')
     CompanyDeptcsv_writer = csv.writer(CompanyDeptCsvFile)
## Sales Department     
     salesFileName = "dataSource/SalesDept.csv"
     fileStatus = FileChecking(salesFileName)
     if (fileStatus == FILE_EXIST):
          ahNew = []
          salesFile = open(salesFileName, "r", newline='', encoding='UTF8') 
          ahRecords = csv.reader(salesFile)
          header = next(ahRecords)
          print (header[0], header[1], header[2], header[3])
          rec = 0
          for ahrow in ahRecords:
               ahNew.append(AccountHolder(ahrow[0], ahrow[1], ahrow[2], ahrow[3], ahrow[4]))
               rec = rec + 1
     salesFile.close()
     deptHeader = AHDeptHeader("Sales", len(ahNew))
     currentDept = deptAH(deptHeader, ahNew)       
     currentDept.DisplayDept()   
     header = ['HolderName', 'Address', 'Profession', 'BirthDay']
     deptHeadArray = [deptHeader.DeptName , deptHeader.NoOfAH]
     CompanyDeptcsv_writer.writerow(deptHeadArray)
     CompanyDeptcsv_writer.writerow(header)
     for nextAH in currentDept.deptAhs:
          CompanyDeptcsv_writer.writerow([nextAH.getTitle(), \
                    nextAH.getHolderName(), \
                    nextAH.getProfession(), \
                    nextAH.getBirthday()])
## Accounting Department
#actually just a duplicate from sales department
          
     accounFileName = "dataSource/AccountDept.csv"
     fileStatus = FileChecking(accounFileName)
     if (fileStatus == FILE_EXIST):
          ahNew = []
          accounFile = open(accounFileName, "r", newline='', encoding='UTF8') 
          ahRecords = csv.reader(accounFile)
          header = next(ahRecords)
          print (header[0], header[1], header[2], header[3])
          rec = 0
          for ahrow in ahRecords:
               ahNew.append(AccountHolder(ahrow[0], ahrow[1], ahrow[2], ahrow[3], ahrow[4]))
               rec = rec + 1
     accounFile.close()
     deptHeader = AHDeptHeader("Account", len(ahNew))
     currentDept = deptAH(deptHeader, ahNew)       
     currentDept.DisplayDept()   
     header = ['HolderName', 'Address', 'Profession', 'BirthDay']
     deptHeadArray = [deptHeader.DeptName , deptHeader.NoOfAH]
     CompanyDeptcsv_writer.writerow(deptHeadArray)
     CompanyDeptcsv_writer.writerow(header)
     for nextAH in currentDept.deptAhs:
         CompanyDeptcsv_writer.writerow([nextAH.getTitle(), \
                    nextAH.getHolderName(), \
                    nextAH.getProfession(), \
                    nextAH.getBirthday()])

## Logistic Department
     logisticFileName = "dataSource/LogisticDept.csv"
     fileStatus = FileChecking(logisticFileName)
     if (fileStatus == FILE_EXIST):
          ahNew = []
          logisticFile = open(logisticFileName, "r", newline='', encoding='UTF8') 
          ahRecords = csv.reader(logisticFile)
          header = next(ahRecords)
          print (header[0], header[1], header[2], header[3])
          rec = 0
          for ahrow in ahRecords:
               ahNew.append(AccountHolder(ahrow[0], ahrow[1], ahrow[2], ahrow[3], ahrow[4]))
               rec = rec + 1
     logisticFile.close()
     deptHeader = AHDeptHeader("Logistic", len(ahNew))
     currentDept = deptAH(deptHeader, ahNew)       
     currentDept.DisplayDept()   
     header = ['HolderName', 'Address', 'Profession', 'BirthDay']
     deptHeadArray = [deptHeader.DeptName , deptHeader.NoOfAH]
     CompanyDeptcsv_writer.writerow(deptHeadArray)
     CompanyDeptcsv_writer.writerow(header)
     for nextAH in currentDept.deptAhs:
         CompanyDeptcsv_writer.writerow([nextAH.getTitle(), \
                    nextAH.getHolderName(), \
                    nextAH.getProfession(), \
                    nextAH.getBirthday()])

     CompanyDeptCsvFile.close()

     
     
#Driver
main()
