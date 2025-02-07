# -1 water
# 0 snake
# 1 gun
import random
play_again=True
dict={"Snake":0, "Water":-1, "Gun":1}
rev_dict={0:"Snake", 1:"Gun", -1:"Water"}
print('Welcome!')
def Game():
    choice=input("Enter your choice: ").title()
    if choice not in dict:
        print("Invalid choice")
    else:
        computer=random.choice([0,-1,1])
        you=dict[choice]
        print(f"Computer chose {rev_dict[computer]} and you chose {choice}")
        if(computer==you):
            print("Its a tie")
        elif (computer==1 and you==0) or (computer==0 and you==-1) or (computer==-1 and you==1):
            print("You lose!")
        else:
            print("You win")
        
while(play_again):
    Game()
    repeat=input("Do you want to play again? ").title()
    if repeat=="No":
        print("Thankyou for playing")
        play_again=False