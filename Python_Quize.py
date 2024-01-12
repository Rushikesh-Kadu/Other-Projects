from colorama import Fore
import random
print()
answer={1:'GUIDO VAN ROSSUM',2:1994,3:'DEFAULT',4:'COMPLEX',5:'IMPORT',6:'LIST OF STRING',
        7:'SEETA',8:'NO',9:'YES',10:'TYPEERROR',11:'YES',12:'IN PRIVATE HEAP SPACE',13:'YES',
        14:'NO',15:'IN C LANGUAGE'}
print(Fore.CYAN+"Welcome to Python Quize")
print(Fore.RED+"Disclamer : ",end='')
print(Fore.GREEN+"1.Randomnly 5 Questions will Display on terminal u have to answer correctly\n2.If ur answer is correct then u will get one point\n2.else 1 point will diduct from ur score")
while 1:
    Que_No=set()
    while len(Que_No)!=5:
        Q=random.randint(1,15)
        Que_No.add(Q)
    Que_No=list(Que_No)
    index=0
    score=0
    f=open('H:\Windows\Bitmap c\Empty\Projects\Python Project\Questions.txt','r')
    while index<=4:
        try:
            for line in f.readlines():
                if line.startswith('0'+str(Que_No[index])) or line.startswith(str(Que_No[index])):
                    print(Fore.MAGENTA+"\n",index+1,line[3::]+Fore.WHITE,end='')
                    ans=input(" Enter Ur Answer:").upper()
                    if answer[Que_No[index]] in ans:
                        print(Fore.WHITE+"\n  Correct")
                        score+=1
                    else:
                        print(Fore.RED+"\n  Wrong!!!")
                        if score>0:
                            score-=1
                    index+=1
        except:
            break
    if index>4:
        print(Fore.WHITE+"\nYour Score is",score)
        res=input("Wants to play again (Yes/No):").upper()
        if res=='YES':
            pass
        else:
            break
f.close()
