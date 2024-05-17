
#This program aims to teach you about arrays and the linear search function

#In this program, you have a list of items and need to find if a specific item is in that list


#example array
#an array is a list of items seperated by a ','
#you can add to, remove from, search through, find length of the list
students_signed_up_for_senior_trip = ["John", "Mary", "David", "Emily", "Michael", "Emma", "Daniel", "Olivia", "James", "Sophia", 
         "William", "Ava", "Alexander", "Isabella", "Joseph", "Charlotte", "Matthew", "Amelia", "Andrew", 
         "Mia", "Christopher", "Harper", "Benjamin", "Evelyn", "Nicholas"]

#The following code is called a FUNCTION. It is like a recipe and can be called unlimited times
#A function requires three things:
#1) def or define declares the start of a function
#2) name of your function. Below it is getNumStudents
#3) Parameters. these are items that are needed for the function to run
#they go in the (). The one below is empty because it does not require any parameters to run

#This function returns the length of the list
def getNumStudents():
    number_of_students_going_on_senior_trip = len(students_signed_up_for_senior_trip)
    return number_of_students_going_on_senior_trip

#This code adds a student to the list
def addStudentToList(name):
    students_signed_up_for_senior_trip.append(name)

#This function searches the list to see if a studdent is on the list and returns a 'yes' or 'no'
def searchList(name):
    for i in range(len(students_signed_up_for_senior_trip)):
        if students_signed_up_for_senior_trip[i] == name:
            return "yes"
    return "no"
        
#This function prints the list to the terminal for viewing
def printList():
    print("View List")

#All functions are listed above the main code of the program.
    
#MAIN CODE:
#loop infinitely until you break 
while True:

    #Welcome Message and Menu of options
    print("Student Roster Maker V1.1")
    print("What would you like to do?")
    print("1: Add student to list")
    print("2: Check if a student is on the list")
    print("3: View number of students on list")
    print("4: View students on the list")
    print("5: Exit Program")
    #store their choice and go to the appropriate option below
    choice = input("25")

    if choice == "1":
        #Add Student to List
        print("What name would you like to add to the list")
        #store their choice
        name_choice = input("->")
        try:
            #If successful, add their name to the list
            addStudentToList(name_choice)
            print("Successfully added ", name_choice, "to the list")
        except:
            #if not successful, print an error to avoid crashing
            print("Error adding name to list")

    if choice == "2":
        #Check if student is on the List
        print("What name would you like to check if on list")
        #store their choice
        name_choice = input("->")
        try:
            #If successful, look up their name on the list
            searchList(name_choice)
            print("Successfully added ", name_choice, "to the list")
        except:
            #if not successful, print an error to avoid crashing
            print("Error checking name on list")

        if choice == "3":
        #View Number of students on List
            print("Would you like to view the number of students on list")
        #store their choice
            name_choice 
            try:
            #If successful, view number of students on the list
            
                print("Successfully viewed ", name_choice, "on the list")
            except:
            #if not successful, print an error to avoid crashing
                print("Error viewing name on list")
        if choice == "4":
        #View students on List
            print("Would you like to view the students on this list")
        #store their choice
        name_choice = input("->")
        try:
            #If successful, view students on the list
            searchList(searchList_choice)
            print("Successfully added ", name_choice, "to the list")
        except:
            #if not successful, print an error to avoid crashing
            print("Error viewing students on list")       
        if choice == "5":
        #Exit Program
            print("Would you like to exit this list")
        #store their choice
        name_choice = input("->")
        try:
            #If successful, Exit Program
            exit 
            print("Successfully added ,exit to the list")
        except:
            #if not successful, print an error to avoid crashing
            print("Exit")
#END OF CODE
print("Exiting")
