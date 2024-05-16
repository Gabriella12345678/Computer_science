#HOMEROOM ROSTER
#This program will keep track of students
#It will perform the following tasks 1)see names 2) see basic info 3)see what grade their in

#Create an object called Student
class Student:
    def __init__(self,name,address,locker_number,id,grade,age):
       self.name = name
       self.locker_number = locker_number
       self.grade = grade
       self.id = id
       self.age = age
       self.address = address

#Create the student list array:
list_of_homeroom_students = []

#Functions

def addToHomeroom():
     #Creates a student. Adds them to the roster
    #Has properties:name,locker number,ID,grade,age,address

    #Name
    print("What is their assigned locker number:")
def getNumberOfStudentsInHomeroom():
    numberOfStudentsInHomeroom(list_of_homeroom_students)
def searchForStudentInHomeroom(student):
    pass
def searchStudentAddress(student):
    pass
def getListOfStudents():
    pass
def getStudentID(student):
    pass

#MAIN CODE
while True:
    print("What would you like to do:")
    print("1: View Homeroom roster")
    print("2: Add student to Homeroom") 
    print("3: Remove student's ID number")
    print("4: get a student's ID number")
    print("5: get number of students in homeroom")
    print("6:Search for student on list")
    print("7:Exit Program")
    choice = int(input("->"))
    if choice == "1":
      new_student = Student(name,lockernumber,ID grade,age,address)
      print("new student created with this information")
      print("name:", new_student )
      print("locker number")
      print("ID Number")
      print("Grade")
      print("Age")
      print("Address")
        #View Homeroom Roster
      
    getListOfStudents()
elif choice == 2:
    
elif choice == 3:
     
elif choice == 4:
     
elif choice == 5:
      #Print length of list (#)
print(getNumberOfStudentsInHomeroom(),"students in homeroom")
elif choice == 6:
    
else: 
     print("Selection error has occured try again")
