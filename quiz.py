questions=[["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2],
           ["What is the capital of India? ", "a. Up", "b. Delhi", "c. New Delhi", "d. Goa", 2]]
levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000]

play=True
def game():
    money=0
    for i in range(0,len(questions)):
        print(f"Question for Rs.{levels[i]} is: {questions[i][0]}")
        print(f"{questions[i][1]}\n{questions[i][2]}\n{questions[i][3]}\n{questions[i][4]}")
        
        ans=input("Enter your answer: ").title()
        dict={"UP":1, "Delhi":2, "New Delhi":3,"Goa":4}
        
        if(i==2):
            money=3000
        elif(i==5):
            money=6000
        elif(i==8):
            money=9000
        try:
            if(dict[ans]==questions[i][5]):
                
                print(f"You have won Rs{levels[i]}")
            
            else:
                print('wrong ans')
                print(f"Your price money is Rs{money}")
                break
        except :
            print('wrong ans')
            print(f"Your price money is Rs{money}")
            break
            
while(play==True):
    print("Welcome!")
    game()
            
    again=input(("Do you want to play again?: ")).lower()
    if(again=="yes"):
        play=True
    elif(again=="no"):
        play=False
    else:
        print("Invalid Input")
        break
        
print("Thankyou for playing!")
    
    
    
    
