import random as r 

def play(number_of_times):
    win = 0
    loss = 0
    draw = 0

    #loop to iterate number of times choosen to play
    for i in number_of_times:
        print('enter rock(r), paper(p) or scissors(s):')
        a = r.randint(1, 3)
        e = input()

        #1 is rock
        if (a == 1) and (e == 'r'):
            print('ROCK vs ROCK')
            print('Draw!')
            draw += 1

        elif (a == 1) and (e == 'p'):
            print('PAPER vs ROCK')
            print('Win!')
            win += 1
    
        elif (a == 1) and (e == 's'):
            print('SCISSORS vs ROCK')
            print('Loss!')
            loss += 1

        #2 is paper
        if (a == 2) and (e == 'r'): 
            print('ROCK vs PAPER')
            print('Loss!')
            loss += 1
    
        elif (a == 2) and (e == 'p'):
            print('PAPER vs PAPER')
            print('Draw!')
            draw += 1
    
        elif (a == 2) and (e == 's'):
            print('SCISSORS vs PAPER')
            print('Win!')
            win += 1

        #3 is scissor
        if (a == 3) and (e == 'r'):
            print('ROCK vs SCISSORS') 
            print('Win!')
            win += 1
    
        elif (a == 3) and (e == 'p'):
            print('PAPER vs SCISSORS')
            print('Loss!')
            loss += 1
    
        elif (a == 3) and (e == 's'):
            print('SCISSORS vs SCISSORS')
            draw += 1

    
    if (win > loss) and (win > draw):
        print('Congratulations! You win!')
    elif (loss > win) and (loss > draw):
        print('Sorry! You Loose!')
    elif (draw > win) and (draw > loss):
        print('Its a Tie!!')
    elif draw==win==loss:
        print('Its a Tie!!')
    
    
    
    if (win > loss) and (win > draw):
        print('Congratulations! You win!')
    elif (loss > win) and (loss > draw):
        print('Sorry! You Loose!')
    elif (draw > win) and (draw > loss):
        print('Its a Tie!!')
    elif draw==win==loss:
        print('Its a Tie!!')
    
    
   

    print('\n')
    print('=' * 20)
    print('Total Score:')
    print('=' * 20)
    print('Wins: ' + str(win))
    print('Losses: ' + str(loss))
    print('Draws: ' + str(draw))
   
