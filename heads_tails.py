'''
    author: Adhyayan
    date: 22/08/25
    version: 1
    description: This is about commenting your code
'''
#-------------libraries-------------------
import random   #use randint to get random numbers or choice to select from list

#----------------functions-----------------------
#------------------------------------------------
#This function gets a random number to 
#choose from a list of heads or tails like a coin flip
#------------------------------------------------
def heads_tails():
    user_score = 0
    computer_score = 0
    options = ['Heads', 'Tails']
    while user_score != 2 and computer_score != 2:
        choice = random.randint (0,1)
        computer_guess = options[choice]
        user_guess = str(input("Heads or Tails: "))
        if user_guess == computer_guess:
            print("It was {}, you guessed {}, you won that round" .format(computer_guess, user_guess))
            user_score += 1
        else:
            print("It was {}, you guessed {}, you lost that round" .format(computer_guess, user_guess))
            computer_score +=1 
    #the loops has now ended and it will output won the best of 3 rounds
    if user_score == 2:
        print("{}, you won that game" .format(first_name))
    else:
        print("{}, you lost that game" .format(first_name))

#-------------main program----------------------------------
valid = True #looping my validation
print("Hi! Welcome to my Heads or Tails game") #greeting 
first_name = str(input("What is your name: "))  

#validating the user input for age
while(valid):
    try:
        age = int(input("What is your age: ")) #changing string input to integer 1-18   1 and 18 plus test 0 and 19
    except:
        print('You did not enter a valid number')
        continue
    
    if (age >= 12 and age <= 65): #range check for merit
        if (age == None and age.isdecimal()):
        #valid = False
            break #jumping statemant leaves the loop
    else:
        print('You enter an age out of range from 12-65')

heads_tails() #calling a function with no parameter
