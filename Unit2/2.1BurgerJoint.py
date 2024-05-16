#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Southern burger $6.80")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: SOUTHERN BURGER
        elif burgerChoice == "4":
            totalCost = totalCost+ 6.80
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)

            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("sides")
       
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following sides:")
        print("1: Apples 0.50")
        print("2: Fries $3.00")
        print("3: Cheese Fries (Extra cheesy) $2.75")
        sidesChoice = input("What would you like (input a number 1-3): ")
         #Side 1: Apples
        if sidesChoice == "1":
            totalCost = totalCost + 0.50
            print("You added Apples to your order")
            print("Your total cost so far: $", totalCost)

        #Side 2: Fries
        elif sidesChoice == "2":
            totalCost = totalCost + 3.00
            print("You added Fries to your order")
            print("Your total cost so far: $", totalCost)

        #Side 3: Cheesy Fries (Extra Cheesy)
        elif sidesChoice == "3":
            totalCost = totalCost+ 2.75
            print("You added Cheesy Fries to your order")
            print("Your total cost so far: $", totalCost)
    elif menu == "Drinks":
        print("drinks")
    
       
        #IF THEY WANT TO ADD A DRINK:
        print("We offer the following sides:")
        print("1: Chocolate Milk 1.50")
        print("2: Bahahahaha Blast $1.50")
        print("3:Mountain Dew $1.75")
        drinksChoice = input("What would you like (input a number 1-3): ")
         #Drink 1: Chocolate Milk
        if drinksChoice == "1":
            totalCost = totalCost + 0.50
            print("You added Chocolate Milk to your order")
            print("Your total cost so far: $", totalCost)

        #Drink 2: Bahahahaha Blast
        elif drinksChoice == "2":
            totalCost = totalCost + 1.75
            print("You added a Bahahahaha Blast to your order")
            print("Your total cost so far: $", totalCost)

        #Drink 3: Mountain Dew
        elif drinksChoice == "3":
            totalCost = totalCost+ 1.50
            print("You added Mountain Dew to your order")
            print("Your total cost so far: $", totalCost)
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        #Finish this section to give you a grand total as well as print your complete order
        print("order finished")
        print("You have ordered")
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        grandTotal = totalCost + totalTax
        print("Grand Total: $",grandTotal)
        
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
