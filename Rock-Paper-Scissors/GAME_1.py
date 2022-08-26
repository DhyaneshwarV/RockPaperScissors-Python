import random
import time
string='\t\t\t\tROCK_PAPER_SCISSOR'
#print(string.center(20,' '))
print("\n\n")
print('INSTRUCTIONS:\nPress \'1\' for Rock\nPress \'2\' for Paper\nPress \'3\' for Scissors\n\n')   
print('RULES:\nRock smashes scissors\nPaper covers rock\nScissors cut paper\n\n')
def Game():
    number_of_rounds=int(input('Enter the number of rounds:'))
    chance=0
    computer_point=0
    player_point=0
    rounds=0
    while chance<number_of_rounds:
        print('Lets go!')
        time.sleep(1)
        print('ROCK...')
        time.sleep(1)
        print('PAPER....')
        time.sleep(1)
        print('SCISSORS.....\n')
        player_choice=int(input('Enter your choice:1-ROCK|2-PAPER|3-SCISSORS\n'))
        computer_choice=random.randint(1,3)
        rounds+=1
        print(f'ROUND {rounds}')  
        #if both player and computer chooses same
        if computer_choice==1 and player_choice==1:
            print('It\'s a tie\nBoth computer and player choosen Rock\nEach one of them given 0 piont\n')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        elif computer_choice==2 and player_choice==2:
            print('It\'s a tie\nBoth computer and player choosen Paper\nEach one of them given 0 piont\n')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        elif computer_choice==3 and player_choice==3:
            print('It\'s a tie\nBoth computer and player choosen Scissors\nEach oneof them given 0 piont\n')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        #if player choice is 1
        elif player_choice==1 and computer_choice==2:
            computer_point+=1
            print(f'Player choice is Rock and Computer choice is Paper')
            print('Computer Wins\n1 point to computer')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        elif player_choice==1 and computer_choice==3:
            player_point+=1
            print(f'Player choice is Rock and Computer choice is Scissors')
            print('Player Wins\n1 point to player')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        #if player choice is 2
        elif player_choice==2 and computer_choice==1:
            player_point+=1
            print(f'Player choice is Paper and Computer choice is Rock')
            print('Player Wins\n1 point to player')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        elif player_choice==2 and computer_choice==3:
            computer_point+=1
            print(f'Player choice is Paper and Computer choice is Scissors')
            print('Computer Wins\n1 point to computer')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        #if player choice is 3
        elif player_choice==3 and computer_choice==1:
            computer_point+=1
            print(f'Player choice is Scissors and Computer choice is Rock')
            print('Computer Wins\n1 point to computer')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        elif player_choice==3 and computer_choice==2:
            player_point+=1
            print(f'Player choice is Scissors and Computer choice is Paper')
            print('Player Wins\n1 point to player')
            print('________________________\n')
            print(f'Score Board of round {rounds}:\ncomputer:{computer_point} point\nplayer:{player_point} point')
            print('________________________\n')
        else: 
            print('Enter a valid choice')
        chance=chance+1
    #print("====================================================================================================================")
    g='GAME-OVER'
    print(g.center(100,"="))
    print('________________________')
    print(f'Final_scores:\ncomputer:{computer_point} point\nplayer:{player_point}')
    if player_point==computer_point:
        print('The match is a tie')
    elif player_point>computer_point:
        print('Congratulation! this game is won by the player')
    else:
        print('This game won by computer\nBetter luck next time')
    print('________________________\n\n')
    play=int(input('PLAY_AGAIN:(Yes/No)?\nFor Yes press \'1\'For No press \'2\':'))
    if play==1:
        print('RESTARTING THE GAME.......')
        time.sleep(3)
        Game()
Game()