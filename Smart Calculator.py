import speech_recognition as sr
responses=['Welcome To Smart Calculator','My Name is Smarty','Thanks',
           'Sorry,This is Beyond My Ability']

def extract_numbers_from_text(text):
    l=[]
    for x in text.split(' '):
        try:
            l.append(float(x))
        except ValueError:
            pass
    return l

def lcm(a,b):
    L= a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
    L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
    H-=1

def big(a,b):
    return (a if a>b else b)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def end():
    print(responses[2])
    input('Press Enter Key To Exit')
    exit()

def myName():
    print(responses[1])

def sorry():
    print(responses[3])

def help():
    print("List of Commands Are:")
    for k in operations:
        print(k)
    for k in commands:
        print(k)

def cal(text):
            for word in text.split(' '):
                if word.upper() in operations.keys():
                    try:
                        l=extract_numbers_from_text(text)
                        r=operations[word.upper()](l[0],l[1])
                        print(r)
                    except:
                        print("Something is wrong please retry")
                    finally:
                        break
                elif word.upper() in commands.keys():
                    commands[word.upper()]()
                    break
            else:
                 sorry()

operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"BERIJ":add,
"MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub,"SUB":sub,
"DIFFERENCE":sub,"PRODUCT":mul,'MODULUS':mod,'REMAINDER':mod,'MOD':mod,
 "MULTIPLICATION":mul,"MULTIPLY":mul,"MUL":mul,
"DIVIDE":div,"DIVISION":div,"DIV":div, "LCM":lcm,"HCF":hcf,
"BIG":big,"MAX":big,"GREATER":big
 }
commands={"NAME":myName,"END":end,"EXIT":end,"CLOSE":end,"HELP":help}

def main():
    print(responses[0])
    print(responses[1])
    print("\n1.Text Mode ")
    print("2.Speak Mode ")
    c=int(input("Enter Your Choice:"))
    if c==2:
        while True:
             text=''
             r=sr.Recognizer()
             with sr.Microphone() as source:
                 print("Speak Anything")
                 audio=r.listen(source)
                 #try:
                 text=r.recognize_google(audio)
                 print("You Speak:",text)
                 #except:
                  #   print("Sorry Could not recognize your voice")
                 cal(text)
    else:
        while True:
            print()
            text=input("Enter some text: ")
            cal(text)       
         
main()
