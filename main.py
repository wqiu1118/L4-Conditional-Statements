 isHungry = input("Y/N: Are you hungry? ")
isBored = input("Y/N: Are you bored? ")
if (isHungry == "Y" or isHungry == "y"):
  print("Go eat")

else: 
  print("Don't eat")
if(isBored == "Y" or isBored == "y"): 
  print ("Go to sleep")
else: 
  print("Do nothing")

userNumber = int(input("Give me a number: "))
if(userNumber >= 0):
  print("Your number is positive")
else:  
  print("Your number is negative") 

#Ask the user for their age. 
#If the user is older than 17, let them know they can watch any movies.
#If they are younger than 17 but older than 13, let them know they can watch G-rated and PG13
#If they are younger than 13, they are only allowed to watch G-rated movies

userAge = int(input("Enter your age: "))

if(userAge >= 17):
  print("You can watch all movies!")
elif(userAge <17 and userAge >= 13): 
  print("You can watch G-rated and PG-13 movies!")
else:
  print("You can only watch G-rated movies.")

# Ask the user for an x and a y value
# Based on the x and y value, output which quadrant they're in

x = int(input("Give me an x value: "))
y = int(input("Give me a y value: "))

if(x > 0 and y > 0): 
  print("You are at Quadrant 1")
elif(x < 0 and y > 0): 
    print("You are at Quadrant 2")
elif(x < 0 and y < 0):
  print("You are at Quadrant 3")
elif( x > 0 and y < 0): 
    print("You are at Quadrant 4")
elif( x == 0 and y == 0): 
    print("You are at The Origin, try to get somewhere")
elif (x != 0 and y == 0): 
    print("You are at the x-axis")
elif (x == 0 and y != 0): 
    print("You are at the y-axis")  