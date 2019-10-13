import random
correct_number = random.randint(0,100)
print (correct_number)
user_guess = int( input("Guess the number "))
number_array = []
number_array.append(user_guess)
count = 1
while (user_guess != correct_number):
    count += 1
    if (user_guess <= correct_number -20 or user_guess >= correct_number +20):
        print ("You are cold!")
    elif ((correct_number -20 < user_guess and user_guess < correct_number -10) or (correct_number+10 < user_guess and user_guess < correct_number +20)):
        print ("You are warm!")
    elif ((user_guess > correct_number -10 or user_guess < correct_number +10)):
        print ("You are red hot!")
   
    if (count > 2):
        last_guess = number_array[-2]
        if (abs(correct_number - user_guess) > abs(correct_number - last_guess)):
            print ("You are getting colder!")
        elif (abs(correct_number - user_guess) < abs(correct_number - last_guess)):
            print ("You are getting warmer!")
    user_guess = int (input("Guess the number "))
    number_array.append(user_guess)
    
print ("You are correct! You got it after" , count , "guesses.")
        
