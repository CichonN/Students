## ----------------------------------------------------------------------------------------------------------------------------------
## Assignment Name:      Student List - Assignment 8
## Name:                 Neina Cichon
## Date:                 2020-07-10
## ----------------------------------------------------------------------------------------------------------------------------------

import Class

#--------------------------------------------------------------------------
#1. Assign Values to Students to Pass in to Graduation
##--------------------------------------------------------------------------


Student1 = Class.Graduation("Neina","Cichon","F", 31, 4.0, 2019, "Y")
Student2 = Class.Graduation("George","Takei","M", 77, 3.7, 2000, "N")
Student3 = Class.Graduation("Phoebe","Buffay","F", 22, 3.0, 2006, "Y")
Student4 = Class.Graduation("James","Kirk","M", 55, 3.8, 1999, "N")
Student5 = Class.Graduation("Michael","Scott","M", 51, 2.0, 2010)


#--------------------------------------------------------------------------
#1. Display Results 
#--------------------------------------------------------------------------

print(str(Student1))
print("The Average GPA is: ", (Class.stuGPATotal/Class.stuStudentCount))
print("The Average Age of Female Students is: ", (Class.stuFemaleAgeTotal/Class.stuFemaleCount))
print("The Average Age of Male Students is: ", (Class.stuMaleAgeTotal/Class.stuMaleCount))
print("The Female Count is: ", Class.stuFemaleCount)
print("The Male Count is: ", Class.stuMaleCount)
print("The Total Number of Female Students with a job is: ", Class.gradTotalFemaleJobs)
print("The Total Number of Male Students with a job is: ", Class.gradTotalMaleJobs)


