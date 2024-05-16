print ("Fail Calculator")
print ("This app develops a code that creates a calculator that tells the user they failed as assignment and tells their grade")
print ("How many points this grade was out of?")
print ("How many points did you score?")
x = input("score you got: ")
y=input("Total Score: ")
z =int(x)/int(y)* 100
print(z) 
print ("Your Grade is " , z , "%")
if z >= 60:
    print ("You Passed")
else: 
    print("You Failed")
