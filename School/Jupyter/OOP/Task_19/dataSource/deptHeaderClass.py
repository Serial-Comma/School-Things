# deptHeaderClass.py
# Version: 19.01  Date: 02-August-2022 Programmer: Fong KK
## ***** Module for data file header class *****
    
# Constants for information of department
DEPT_NAME = 'DEPARTMENT'
DEPT_NAME_MIN = 5
DEPT_NAME_MAX = 10
DEPT_ACC_MIN = 1
DEPT_ACC_MAX = 1000

class AHDeptHeader:
     def __init__(self, DeptName = DEPT_NAME, NoOfAH = DEPT_ACC_MIN):  
          self.DeptName = DeptName
          self.NoOfAH = NoOfAH #Range 1 - 1000
      ### validation of DeptName
          self.DeptName = DEPT_NAME
          if self.checkDeptName(DeptName)== True:
               self.DeptName = DeptName    
          self.NoOfAH = DEPT_ACC_MIN    # DEPT_ACC_MIN = 1
          if self.checkNoOfAH(NoOfAH) == True:
               self.NoOfAH = NoOfAH
     def __str__(self):
          return f"Deppartment name: {self.DeptName} Number of employees: {self.NoOfEmployees}"
     def checkDeptName(self, DeptName):
          Valid_flag = True
          if len(DeptName) < DEPT_NAME_MIN or len(DeptName) > DEPT_ACC_MAX:
               print(f"\tTry again! '{DeptName}': {DEPT_NAME_MIN} to "\
                     f"{DEPT_NAME_MAX} characters for department name.")
               Valid_flag = False
          elif not DeptName[0].isupper(): #The first character is an upper case letter
               print (f"\tError! '{DeptName}': Department Name: "\
                      f"The first character is a capital letter.")
               Valid_flag = False
          return Valid_flag
     def checkNoOfAH(self, NoOfAH):
          Valid_flag = True
          #Validation rule: Data type - int
          if (type(int(NoOfAH))) != int:
               print (f"\tError! Number Of account holders is not integer!")
               Valid_flag = False
          #Validation rule: NoOfEmployees is not negative
          elif NoOfAH < 0:
               print (f"\tError! Number Of account holders cannot be negative.")
               Valid_flag = False           
          #Validation rule: Range check
          elif NoOfAH < DEPT_ACC_MIN or NoOfAH > DEPT_ACC_MAX:
               print (f"\tError! Number Of account holders is between "\
                      f"{DEPT_ACC_MIN} to {DEPT_ACC_MAX}.")
               Valid_flag = False      
          return Valid_flag
