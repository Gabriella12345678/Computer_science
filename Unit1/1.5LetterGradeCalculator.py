print (" Calculator")
print ("This app develops a code that creates a calculator that tells the user they failed as assignment and tells their grade")
print ("How many points this grade was out of?")
print ("How many points did you score?")
x = input("score you got: ")
y=input("Total Score: ")
z =int(x)/int(y)* 100
print(z) 
print ("Your Grade is " , z , "%")

if z >= 90:
    print ("You got an A = 100%")
elif z >=80:
    print ("You got an B = 80%")
elif z >=70:
    print ("You got an C =70%")
elif z >=60:
    print ("You got an D = 60%")
elif z >=50:
    print ("You got an F = 50%")


else: 
    print("You Failed")
