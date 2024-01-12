responses=["Welcome to smart Calculator","My Name is Smarty","Thanks","Sorry,This is beyond my ability","Fine"]
def ExtractNumbersFromText(text):
    l=[]
    for x in text.split(' '):
        try:
            l.append(float(x))
        except ValueError:
            pass
    return l;

def LCM(a,b):
    L=a if a>b else b;
    while(L<=a*b):
        if(L%a==0 and L%b==0):
            return L
        L+=1;

def HCF(a,b):
    H=a if a<b else b
    while(H>=1):
        if(a%H==0 and b%H==0):
            return H
        H-=1;

def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def mul(a,b):
    return a*b;
def div(a,b):
    return a/b;
def mod(a,b):
    return a%b;
def max(a,b):
    return a if a>b else b
def min(a,b):
    return a if a<b else b
def myName():
    print(responses[1])

def end():
    print(responses[2])
    input("Press Enter Key To Exit")
    exit()

def sorry():
    print(responses[3]);

def how():
    print(responses[4])

operations={"ADDITION":add,"ADD":add,"PLUS":add,"SUM":add,"SUBTRACT":sub,"SUBTRACTION":sub,"SUB":sub,"MINUS":sub,"DIFFERENCE":sub,"DIVIDE":div,
            "DIVISION":div,"DIV":div,"DIVIDES":div,"MULTIPLICATION":mul,"MULTIPLY":mul,"MUL":mul,"INTO":mul,"MODULES":mod,"REMINDER":mod,
            "GREATEST":max,"MAX":max,"MAXIMUM":max,"MINIMUM":min,"MIN":min,"SMALLEST":min}

commands={"NAME":myName,"MYNAME":myName,"SELF":myName,"END":end,"EXIT":end,"CLOSE":end,"HOW":how}


