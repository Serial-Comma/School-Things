## Task_13.py
## Version: 13.01  Date: 28-July-2022 Programmer: Fong KK
## ***** Module: Demonstration of the behaviour of private attribute type *****
import csv
##Constant section
from dataSource import aC

##Validation check requirements for Title
TITLE_LENGTH=2
TITLE_1ST_CHAR='T'
TITLE_2ND_RANGE='0123456789'

class AccountHolder:
   ## Constructor 
   def __init__(self, hdTilt=aC.HD_TITLE, hdName=aC.HD_NAME, \
                hdAddr=aC.HD_ADDRESS, hdProf=aC.HD_PROFESSION,\
                hdBday=aC.HD_BIRTHDAY):
      ### Instance attributes/Data members
      self.__Title    = aC.HD_TITLE #Private, set default value
      if hdTilt != aC.HD_TITLE:
         self.setTitle(hdTilt)
      
      self.HolderName = hdName  ##Public 
      self.Address    = hdAddr  ##Public
      self.Profession = hdProf  ##Public 
      self.BirthDay   = hdBday  ##Public

   #----- Accessor (Getter) Method
   def getTitle(self):
      return self.__Title
   #----- Mutator (Setter) Method
   def setTitle(self,newTitle):
      validFlag= True
     
      if self.is_Title_valid(newTitle)==True:
         self.__Title=newTitle
      else:
         validFlag=False
         return validFlag
   #Val-Check   
   def is_Title_valid(self,Title): ##validation check fore title'
      validFlag=True
      if len(Title)!=TITLE_LENGTH:
         validFlag=False
         print(f"Length of Title must be 2!")
      elif Title[0]!=TITLE_1ST_CHAR:
         validFlag=False
         print(f'The first character must be T!')
      elif not (Title[1] in TITLE_2ND_RANGE):
         validFlag=False
         print(f'The second character must be one of 0 to 9!')
      return validFlag
      
   def NameCard(self):
        return f"{'='*50}\n"\
               f"\t{self.__Title}. {self.HolderName}\n"\
               f"\t{self.Address}\n\t{self.Profession}\n"\
               f"{'='*50}"
   def __str__(self):
        return f"Title: {self.__Title}\t" \
               f"|Name: {self.HolderName}\t" \
               f"|Address: {self.Address}\t|Profession: {self.Profession}\t"\
               f"|BirthDay: {self.BirthDay}" 
      ## Destructor
   def __del__ (self):
      return True
   def Display(self): # Use of Dictionary for TitleTypes
      print(f"{'Account holder record ':24}\n"
             f"{'-' * 70}\n"
             f"{'Title: ' + aC.TitleTypes[self.__Title]:34}"
             f"{'Date of birth: ' + self.BirthDay:>34}\n"
             f"{'Name: ' + self.HolderName:30}\n"
             f"{'Profession: ' + self.Profession:22}\n"
             f"{'Address: ' + self.Address:18}\n"
             f"{'-' * 70}")
      return ''
