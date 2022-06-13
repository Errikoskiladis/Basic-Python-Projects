restart="1"
from IPython.display import clear_output
while restart=='1': 
    move=["","","","","","","","",""]

    checklist=["1","2","3","4","5","6","7","8","9"]
    print("W E L C O M E    T O    T I C    T A C   T O E   b y    E r r i k. K")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    player_1=input("Write the name of the first player and press enter: ")
    clear_output()
    player_2=input("Now write the name of the second player and press enter: ")
    clear_output()
    print("This are your available moves")
    print("")
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print('{0:^8} | {1:^8} | {2:^8}'.format('1','2','3'))
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print("------------------------------")
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print('{0:^8} | {1:^8} | {2:^8}'.format("4","5","6"))
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print("------------------------------")
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print('{0:^8} | {1:^8} | {2:^8}'.format("7","8","9"))
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print("")
    print("This is the table till now")
    print("")

    ST=["","","","","","","","",""]

    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print('{0:^8} | {1:^8} | {2:^8}'.format(ST[0],ST[1],ST[2]))
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print("------------------------------")
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print('{0:^8} | {1:^8} | {2:^8}'.format(ST[3],ST[4],ST[5]))
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print("------------------------------")
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
    print('{0:^8} | {1:^8} | {2:^8}'.format(ST[6],ST[7],ST[8]))
    print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))

    checklist=["1","2","3","4","5","6","7","8","9"]
    i=0

    while i<=8:
        if i%2==0:
            move[i]=input(f"{player_1} -X symbol- write the number of the box you want to fill, then press enter: ")
            while (move[i] not in checklist) or (ST[int(move[i])-1]!=""):
                move[i]=input(f"not valid entrance, {player_1} -X symbol- Try again: ")
            else:    
                ST[int(move[i])-1]="X"
                checklist[int(move[i])-1]=""
                if ST[0]==ST[1]==ST[2]=="X" or ST[0]==ST[3]==ST[6]=="X" or ST[3]==ST[4]==ST[5]=="X" or ST[6]==ST[7]==ST[8]=="X" or ST[1]==ST[4]==ST[7]=="X" or ST[2]==ST[5]==ST[8]=="X" or ST[0]==ST[4]==ST[8]=="X" or ST[2]==ST[4]==ST[6]=="X":
                    i=9
                    winner=player_1
                
        else: 
            move[i]=input(f"{player_2} -O symbol- write the number of the box you want to fill, then press enter: ")
            while (move[i] not in checklist) or (ST[int(move[i])-1]!=""):
                move[i]=input(f"not valid entrance, {player_2} -O symbol- Try again:")
            else:
                ST[int(move[i])-1]="O"
                checklist[int(move[i])-1]=""
                if ST[0]==ST[1]==ST[2]=="O" or ST[0]==ST[3]==ST[6]=="O" or ST[3]==ST[4]==ST[5]=="O" or ST[6]==ST[7]==ST[8]=="O" or ST[1]==ST[4]==ST[7]=="O" or ST[2]==ST[5]==ST[8]=="O" or ST[0]==ST[4]==ST[8]=="O" or ST[2]==ST[4]==ST[6]=="O":
                    i=9
                    winner=player_2
        from IPython.display import clear_output
        clear_output()
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("This are your available moves")
        print("")
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print('{0:^8} | {1:^8} | {2:^8}'.format(checklist[0],checklist[1],checklist[2]))
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print("------------------------------")
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print('{0:^8} | {1:^8} | {2:^8}'.format(checklist[3],checklist[4],checklist[5]))
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print("------------------------------")
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print('{0:^8} | {1:^8} | {2:^8}'.format(checklist[6],checklist[7],checklist[8]))
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print("")
        print("This is the table till now")
        print("")
        
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print('{0:^8} | {1:^8} | {2:^8}'.format(ST[0],ST[1],ST[2]))
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print("------------------------------")
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print('{0:^8} | {1:^8} | {2:^8}'.format(ST[3],ST[4],ST[5]))
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print("------------------------------")
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        print('{0:^8} | {1:^8} | {2:^8}'.format(ST[6],ST[7],ST[8]))
        print('{0:^8} | {1:^8} | {2:^8}'.format("","",""))
        i+=1

    else:
        if i==10:
            clear_output()
            print("")
            print("")
            print("")
            print(f"the winner is player {winner}") 
            print("")
            print("")
            print("")
        else:
            print("")
            print("")
            print("")
            print(f"{player_1} and {player_2}... It's a DRAW!!! ")
            print("")
            print("")
            print("")
    
    restart=input("PRESS 1 and then PRESS ENTER to restart... Otherwise PRESS any button to close the game: ")