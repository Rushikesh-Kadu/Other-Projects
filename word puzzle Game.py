import random
from colorama import Fore
 
words = ['father','break','routine','range','aeroplane','listen','saw','cat', 'special','beautiful','wonderful','sorry',
   'shut','cry','blem','speech','blush']            # Word of Puzzle
msg=['Arrange the letters to form a valid word:','\nCorrect\n','\nWrong\n','Net Score is']      # Messages display in puzzle
while True:
    range=set()
    range.clear()
    while len(range)!=5:
        range.add(random.randint(0,16))         # generate random question numbers
    range=list(range)                           # Contains 5 random numbers
    i=0 
    score=0                                     # Contains Score of Player
    while i<5:
        print(Fore.GREEN+msg[0])
        ''.join(random.sample(words[range[i]]),k=len(words[range[i]]))       # shuffle the letters of word fetch from list
        








    
    # while i<5:
    #     print(Fore.GREEN+msg[0])
    #     print(Fore.WHITE+words[range[i]])
    #     ans=input().lower()
    #     if(ans==words_form[words[range[i]]]):
    #         print(msg[1])
    #         score+=1
    #     else:
    #         print(msg[2])
    #         if score!=0:
    #             score-=1
    #     i+=1
    # else:
    #     print(msg[3],score)
    # choice=input('If u wants to play again then Press Y/N:')
    # if choice=='y' or choice=='Y':
    #     print()
    # else:
    #     break


     