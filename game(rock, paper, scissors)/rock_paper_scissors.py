import play_func as p
'''ROCK PAPER SCISSORS'''


#introduction
print('=' * 40)
print('ROCK --- PAPER --- SCISSORS')
print('=' * 40)
print('how many times you want to play?:')
number_of_times = range(int(input()))
play_again = True

#loop set to enable multiple chance of play
while play_again:
    #play function
    p.play(number_of_times)

#play again prompt   
    print('\nPLAY AGAIN?:')
    play = input()
    if (play == 'Y') or (play == 'y'):
        play_again = True
    
    elif (play == 'N') or (play == 'n'):
        play_again = False
        break

print('GAME ENDED!!!')

'''ANA3RO'''

