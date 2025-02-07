import random

limit=5
score=0
p=True
inv=False
def game():
    comp=random.randint(1,101)
    rounds=0
    while(rounds<=limit):
        a=int(input("Enter your guess from 1 to 100: "))
        if(a>100):
            print("Invalid choice")
            global inv
            inv=True
            break
        if(a==comp):
            print('Perfect guess!')
            global score
            score=score+1
            global ans
            ans=True
            break
            
        elif(a<comp):
            print("Too low!")
        elif(a>comp):
            print('Too high!')
        rounds+=1
    if(inv):
        pass
    elif(ans==False):
        print("You are out of limits")
    
while(p):
    ans=False
    print("Welcome")
    game()
    again=input("Do you want to play again? ").lower()
    if(again=="yes"):
        p=True
    elif(again=="no"):
        p=False
        
    
    else:
        print("Invalid choice")
        p=False
print(f"Your score is: {score}")
print("Thankyou for playing!")
        
        