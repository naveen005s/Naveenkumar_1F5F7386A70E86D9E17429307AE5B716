import random
class A:
    lst1= [1,2,3,4,5,6,7,8,9,10]
    global chances_1
    chances_1= 5
    global no_of_chances_1
    no_of_chances_1= 0
    global your_runs
    your_runs= 0
    print ("-----------------------------------------------\nplayer1 Batting\n")
    while no_of_chances_1 < chances_1:
        runs= int(input("Enter Runs for Your Batting Turn: "))
        player2 = random.choice(lst1)
        if runs==player2:
            print ("Your Guess: ",runs,",player2 Guess: ",player2)
            print ("You are Out. Your Total Runs= ", your_runs,"\n")
            break
        elif runs>10:
            print ("ALERT!! Support No only till 10\n")
            continue
        else:
            your_runs= your_runs+runs
            print ("Your Guess: ",runs,",player2 Guess: ",player2)
            print ("Your runs Now are: ",your_runs,"\n")
        no_of_chances_1= no_of_chances_1 + 1  
class B(A):
    lst2= [1,2,3,4,5,6,7,8,9,10]
    global chances_2
    chances_2= 5
    global no_of_chances_2
    no_of_chances_2= 0
    global player2
    player2= 0
    print ("-----------------------------------------------")
    print ("player2 Batting-\n")
    while no_of_chances_2 < chances_2:
        bowl= int(input("Enter Runs for Your Bowling Turn: "))
        player1 = random.choice(lst2)
        if player1==bowl:
            print ("player1 : ",player1,"Your Guess: ",bowl)
            print ("The player2 is Out. player2 Runs= ",player2,"\n")
            break
        else:
            player2= player2+player1
            print ("player1 : ",player1,"Your Guess: ",bowl)
            print ("player1 : ",player2,"\n")
            if player2 > your_runs:
                break
        no_of_chances_2= no_of_chances_2+1
        
class c(B):
    print ("\n-----------------------------------------------\nRESULTS: ")
    if player2 < your_runs:
        print ("\nplayer1 won the Game.\n\nYour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]","\nplayer2 Total Runs= ",player2,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")
    elif player2 == your_runs:
        print ("The Game is a Tie")
    else:
        print ("\nplayer2 won the Game.\n\nplayer2 Total Runs= ",player2,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]","\nplayer1 Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")