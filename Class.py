# ----------------------------------------------------------------------------------------------------------------------------------
# Assignment Name:      Student List
# Name:                 Neina Cichon
# Date:                 2020-07-14
# ----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------
#1. Declare Global Variables 
#--------------------------------------------------------------------------
stuStudentCount = 0
stuMaleCount = 0
stuFemaleCount = 0
stuFemaleAgeTotal = 0
stuMaleAgeTotal = 0 
stuGPATotal = 0
gradTotalFemaleJobs = 0
gradTotalMaleJobs = 0
gradStatus = 0


class Person:
    def __init__(self, firstname, lastname, gender, age):
      self.firstname = firstname
      self.lastname = lastname
      self.gender = gender
      self.age = age

      #Counter for total students
      global stuStudentCount
      stuStudentCount += 1

    @property
    def firstname(self):
        return self.__firstname
    @property
    def lastname(self):
        return self.__lastname
    @property
    def gender(self):
        return self.__gender
    @property
    def age(self):
        return self.__age

    #validate name
    @firstname.setter
    def firstname(self, firstname):
        if not firstname.isalpha():
             raise Exception('firstname cannot be a number.')
        else:
            self.__firstname = firstname

    #Validate name
    @lastname.setter
    def lastname(self, lastname):
        if not lastname.isalpha():
            raise Exception('lastname cannot be a number.')
        else:
            self.__lastname = lastname

    #validate gender
    @gender.setter
    def gender(self, gender):
        if gender == 'F':
            self.__gender= gender 
        elif gender == 'M':
            self.__gender= gender
        else:
            raise Exception('Gender is not "F" or "M".')

    #validate age
    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception('age should be greater than 0. The value of age was: {}'.format(age))
        else:
            self._age = age

class Student(Person):

    def __init__(self, firstname, lastname, gender, age, gpa):
        self.gpa = gpa
        Person.__init__(self, firstname, lastname, gender, age)
        
        #Get male and female counts and ages
        global stuGPATotal,stuMaleCount, stuMaleAgeTotal, stuFemaleCount, stuFemaleAgeTotal
        stuGPATotal += gpa
        if (self.gender == 'M'):
            stuMaleCount += 1
            stuMaleAgeTotal += age
        else:
            stuFemaleCount += 1
            stuFemaleAgeTotal += age

    @property
    def gpa(self):
          return self._gpa

    #Validate gpa
    @gpa.setter
    def gpa(self, gpa):
        if gpa < 0 or gpa > 4.0:
            raise Exception('gpa should be between 0 and 4.0. The value of gpa was: {}'.format(gpa))
        else:
            self._gpa = gpa




class Graduation(Student):

    def __init__(self, firstname, lastname, gender, age, gpa, graduationYear, jobStatus = "N"):
        self.graduationYear = graduationYear
        self.jobStatus = jobStatus

        super(Graduation, self).__init__( firstname, lastname, gender, age, gpa)

    # Get Females with jobs
        if (gender == "F"):
            if jobStatus == "Y":
                global gradTotalFemaleJobs
                gradTotalFemaleJobs += 1
    #Get Males with Jobs
        elif gender == "M":
            if jobStatus == "Y":
                global gradTotalMaleJobs
                gradTotalMaleJobs += 1

        @property
        def graduationYear(self):
          return self._graduationYear

        @property
        def jobStatus(self):
          return self._jobStatus

      #Validate Graduation Year as number
        @graduationYear.setter
        def graduationYear(self, graduationYear):
            if graduationYear.isnumeric():
                self._graduationYear = graduationYear
            else:                 
                raise Exception('graduationYear should be an integer. The value of graduationYear was: {}'.format(graduationYear))
        #Validate Job Status
        @jobStatus.setter
        def jobStatus(self, jobStatus):
            if jobStatus == "Y"  or jobStatus == "N":
                self._jobStatus = jobStatus
            else:
                raise Exception('jobStatus was not "Y" or "N". The value of jobStatus was: {}'.format(jobStatus))
    
    #Magic Method to get Graduated Student Count
    def __str__(Graduation):
        return  "Total Graduated Student Count is: "+ str(stuStudentCount)

