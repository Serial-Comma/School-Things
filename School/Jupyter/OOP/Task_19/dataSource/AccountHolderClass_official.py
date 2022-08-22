## AccountHolderClass.py
## Definition of AccountHolder Class
## Validation check requirements for Title
from dataSource import aC
TITLE_LENGTH          = 2
TITLE_1ST_CHAR        = 'T'
TITLE_2ND_RANGE       = '0123456789'
NAME_LENGTH_MIN       = 3
NAME_LENGTH_MAX       = 66
ADDRESS_LENGTH_MIN    = 20
ADDRESS_LENGTH_MAX    = 66
PROFESSION_LENGTH_MIN = 3
PROFESSION_LENGTH_MAX = 40
class AccountHolder:
   DeptMessage='All present up until now.'
   ## Constructor 
   def __init__(self, hdTilt=aC.HD_TITLE, hdName=aC.HD_NAME, \
                hdAddr=aC.HD_ADDRESS, hdProf=aC.HD_PROFESSION,\
                hdBday=aC.HD_BIRTHDAY):
      ### Instance attributes/Data members
      self.__Title = hdTilt             #Private, set default value
     
      self.__HolderName = hdName        #Private, set default value
      if hdName != aC.HD_NAME:
         self.setHolderName(hdName)
      self.__Address = hdAddr           #Private, set default value
      if hdAddr != aC.HD_ADDRESS:
         self.setAddress(hdAddr)
      self.__Profession = hdProf        #Private, set default value
      if hdProf != aC.HD_PROFESSION:
         self.setProfession(hdProf)
      self.__BirthDay = hdBday          #Private, set default value
      if hdBday != aC.HD_BIRTHDAY:
         self.setBirthday(hdBday)        
         
   #---- Accessor (Getter) methodS
   def getTitle(self):
      return self.__Title      
   def getHolderName(self):
      return self.__HolderName
   def getAddress(self):
      return self.__Address
   def getProfession(self):
      return self.__Profession
   def getBirthday(self):
      return self.__Birthday   
   #---- Mutator (Setter) methods
   def setTitle(self, newTitle):
      validFlag = True
      if self.checkTitle(newTitle)== True:
         self.__Title = newTitle
      else:
         validFlag = False
      return validFlag     
   def setHolderName(self, newHolderName):
      validFlag = True
      if self.checkLength('Holder name', newHolderName,\
                NAME_LENGTH_MIN, NAME_LENGTH_MAX)== True:
         self.__HolderName = newHolderName
      else:
         validFlag = False
      return validFlag
   def setAddress(self, newAddress):
      validFlag = True
      if self.checkLength('Address', newAddress, \
              ADDRESS_LENGTH_MIN, ADDRESS_LENGTH_MAX)== True:
         self.__Address = newAddress
      else:
         validFlag = False
      return validFlag
   def setProfession(self, newProfession):
      validFlag = True
      if self.checkLength('Profession', newProfession,\
              PROFESSION_LENGTH_MIN, PROFESSION_LENGTH_MAX)== True:
         self.__Profession = newProfession
      else:
         validFlag = False
      return validFlag
   def setBirthday(self, newBirthday):
      validFlag = True
      if self.checkDate(newBirthday)== True:
         self.__Birthday = newBirthday
      else:
         validFlag = False
      return validFlag
   
   def checkTitle(self, Title): #Validation checks for __Title
      validFlag = True
      if len(Title) != TITLE_LENGTH:            ##Length check
         validFlag = False
         print(f"Length of Title must be 2!")
      elif Title[0] != TITLE_1ST_CHAR:          ##Format check
         validFlag = False
         print(f"Error! First character of Title must be T!")
      elif not ( Title[1] in TITLE_2ND_RANGE):  ##Format check
         validFlag = False
         print(f"Error! Second character of Title must be one of 0 to 9!")         
      return validFlag         
   def checkLength(self, attribureName, newItem, LENGTH_MIN, LENGTH_MAX):
      validFlag = True
      if (len(newItem)< LENGTH_MIN or len(newItem)> LENGTH_MAX):
         print(f"Error! Length of {attribureName} is between \
{LENGTH_MIN} and {LENGTH_MAX}.")
         validFlag = False
      return validFlag  
   def checkDate(self, newDate):
##       print(newDate, type(newDate))
       validFlag = True
       newday = newDate.split('/')
       day = int(newday[0])
       month = int(newday[1])
       year = int(newday[2])
     #checks the range of year input
       if year <= 9999 and year >= 1900:
          if month <= 12 and month >= 1:
             isLeapYear = self.leapYear(year) #if year is leap, isLeapYear = True
             if month in (1,3,5,7,8,10,12) and (day >= 1 and day <= 31): #case of months with 31 days
                 validFlag = True; 
             elif month in (4,6,9,11) and (day >= 1 and day <= 30): #case of months with 30 days
                 validFlag = True
             elif month == 2 and isLeapYear == False and (day >= 1 and day <= 28): #case of non leap year
                 validFlag = True 
             elif month == 2 and isLeapYear == True and (day >= 1 and day <= 29): #case of leap year
                 validFlag = True 
             else:
                 validFlag = False; print(f"Error! Day of Birthday is between 1 and 31!")
          else:
             validFlag = False; print(f"Error! Month of Birthday is between 1 and 12!")
       else:
          validFlag = False; print(f"Error! Year of Birthday is between 1900 and 9999!")
       return validFlag
   def leapYear(self, y):
       validFlag = True
       if (y % 4) == 0:  
           if (y % 100) == 0:  
               if (y % 400) == 0:  
                   validFlag = True #Leap  
               else:  
                   validFlag = False #not Leap  
           else:  
               validFlag = True #Leap  
       else:  
           validFlag = False #not Leap
       return validFlag
   def NameCard(self):
        return f"{'='*50}\n"\
               f"\t{self.__Title}. {self.__HolderName}\n"\
               f"\t{self.__Address}\n\t{self.__Profession}\n"\
               f"{'='*50}"
   def __str__(self):
        return f"Title: {self.__Title}\t" \
               f"|Name: {self.__HolderName}\t" \
               f"|Address: {self.__Address}\t|Profession: {self.__Profession}\t"\
               f"|BirthDay: {self.__BirthDay}" 
      ## Destructor
   def __del__ (self):
      return True
   def Display(self): # Use of Dictionary for TitleTypes
      print(f"{'Account holder record ':24}\n"
             f"{'-' * 70}\n"
             f"{'Title: ' + aC.TitleTypes[self.__Title]:34}"
             f"{'Date of birth: ' + self.__BirthDay:>34}\n"
             f"{'Name: ' + self.__HolderName:30}\n"
             f"{'Profession: ' + self.__Profession:22}\n"
             f"{'Address: ' + self.__Address:18}\n"
             f"{'-' * 70}")
      return ''
