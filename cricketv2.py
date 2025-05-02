import random as r

uwicket=0
pwicket=0
uball=0
uover=0
pball=0
pover=0
uscore=0
pcscore=0
answer = ["YES","yes","y","Y","Yes","yES"]
def batting(over=5):
    global uwicket
    global uball
    global uover
    global uscore
    innings=0
    print("You can hit anything between 0 to 6. Hit hard!")
    input("Press enter to start...")
    while uwicket<11 and innings==0:
        for i in range(over):
            for j in range(6):
                userbat=int(input("HIT->"))
                if userbat>6 or userbat<0 or userbat=='':
                    print("Error buddy! try to play safe next time.")
                    batting()
                cpubowl=r.randint(0,6)
                if userbat==cpubowl:
                    print("OUT!")
                    uwicket+=1
                else:
                    uscore+=userbat
                    print(f"You have scored {userbat}. Now, {5-uball} balls left.")
                uball+=1
            uball=0
            uover+=1
            print(f"The over has ended. Your current score: {uscore}/{uwicket} in {uover} overs")
        print("Final score of the innings is ", uscore, 'by', uwicket, 'wickets')
        if innings==0:
            innings+=1
            bowling(over)
        else:
            print(uscore)
            #MORE TO BE ADDED
def bowling(over=5):
    global pball
    global pwicket
    global pover
    global pcscore
    innings=0
    print("Bowl between 0 to 6. Take as many wickets by guessing the hit of batsman.")
    input("Press enter to start...")
    while pwicket<11 and innings==0:
        for k in range(over):
            for l in range(6):
                userbowl=int(input("BOWL->"))
                if userbowl>6 or userbowl<0 or userbowl=='':
                    print("Error buddy! try to play safe next time.")
                    bowling()
                cpubat=r.randint(0,6)
                if userbowl==cpubat:
                    pwicket+=1
                    print(f"It's an OUT! You have taken {pwicket} wickets in {pball} balls.")
                else:
                    pcscore+=userbowl
                    print(f"Opponent has scored {cpubat} scores in {pwicket} wickets. Now, {5-pball} balls left.")
                pball+=1
            pball=0
            pover+=1
            print(f"The over has ended. You have taken {pwicket} wickets and opponent has scored {pcscore} scores.")
        print(f"Final score of innings is {pwicket} wickets by {pcscore} of opponenet.")
        if innings==0: 
            innings+=1
            batting(over)
        else:
            print(pcscore)
            #MORE TO BE ADDED

def toss():
    #head tail and bat or ball choosing function
    try:
        headtail=int(input("Choose 1 for head and 0 for tail. Skip to quit.\n->"))
        tossresult=r.randint(0,1)
        if headtail==tossresult:
            print('Congratulations you won the toss!')
            userchoose=int(input("Now choose batting or bowling. 1 for bat and 0 for bowl :"))
        elif headtail not in (0,1):
            quit()
        else:
            userchoose=r.randint(0,1)
            print("Sorry you lost the toss.")
    except:
        print("Thanks for playing!")
        quit()
    def choosebattingorbowling():
        try:
            n = int(input("How many overs do you want to play?->"))
            if userchoose==1:
                batting(n)
            elif userchoose==0:
                bowling(n)
            else:
                print("You messed up buddy! Choose again.")
                choosebattingorbowling()
        except:
            print("Please donot mess again!")
            ans = input("wanna quit the game?")
            if ans not in answer:
                choosebattingorbowling()
    choosebattingorbowling()
toss()
