#STONE,PAPER & SCISSOR GAME
Choose=int(input("Enter 1 to Play & Enter 0 to exit the Game: "))
while(Choose==1):
    import random
    ch=input("\nType (S for 'Stone',P for 'Paper',Sr for 'Scissor')\nEnter choice: ")
    Dict1={'S':1,'P':-1,'Sr':0}
    Dict2={1:'Stone',-1:'Paper',0:'Scissor'}
    
    if(ch!='S' and ch!= 'P' and ch!= 'Sr'):
        print("Exitting the Game!!!\n",sep=' ')
        break
    
    You=Dict1[ch]
    Botty=random.choice([1,-1,0])

    print(f"\nYou chosed : *{Dict2[You]}* & Botty chosed: *{Dict2[Botty]}*")

    if(Botty==You):
        print("It's a Draw 🧘‍♂️",sep=' ')
    else:
        if(Botty==-1 and You==1):
            print("You Lost 😉")
        elif(Botty==-1 and You==0):
            print("You Won 🎉")
        elif(Botty==1 and You==-1):
            print("You Won 🎉")
        elif(Botty==1 and You==0):
            print("You Lost 😉")
        elif(Botty==0 and You==1):
            print("You Won 🎉")
        elif(Botty==0 and You==-1):
            print("You Lost 😉")
        elif(Botty==-1 and You==1):
            print("You Lost 😉")
        else:
            print("Choose again!!")
while(Choose==0):
    print("\nGame is Over !!")
    break