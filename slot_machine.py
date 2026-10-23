#take deposit
#ask for bet
#roll the line
#check if any lines connect
# add or deduct money from balance
#loop or exit depending on balance or user input

import random
numbers=[1,2,3,4,5]

def roll():
    line1=random.choice(numbers)
    line2=random.choice(numbers)
    line3=random.choice(numbers)
    print(line1 , line2 , line3)
    return line1, line2, line3

# write a loop to check how many lines connect and then proceed to bet profit or loss
def connecting_lines(line1,line2,line3):
    if line1==line2 or line1==line3 or line2==line3:
        return 2
    elif line1==line2==line3:
        return 3
    else:
        return 0


def deposit():
    balance=int(input("enter the amount you want to deposit: "))
    return balance  

def bet():
    bet_amount=int(input("enter the amount you want to bet: "))
    return bet_amount

def get_number_of_lines():
    lines=int(input("enter the number of lines you want to bet on (0 , 2 or 3): "))
    if lines<1 or lines>3:
        print("invalid number of lines. Please enter a number .")
        return get_number_of_lines()
    return lines

balance=deposit()

def game(balance):
    while True:
        play=input("do you want to play? (y/n): ").lower().strip()
        if play=='y':
            bet_amount=bet()
            lines=get_number_of_lines()
            line1, line2, line3 = roll()
            connecting=connecting_lines(line1, line2 , line3)
            if lines==connecting:
                print("Congratulations!!. You won")
                balance=balance+(bet_amount*lines)
                print(f"current balance : {balance}")
                game(balance)
                
            else:
                print("OOPS!! you lost")
                balance=balance-bet_amount
                print(f"current balance : {balance}")
                game(balance)
            break
        else:
            print("remaining balance: ", balance)
            break


game(balance)