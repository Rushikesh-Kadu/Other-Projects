from MathModule import *
import speech_recognition as s;
print(responses[0])
print(responses[1])
while True:
    print()
    sr=s.Recognizer()
    with s.Microphone() as m:
        print("Speak Anything")
        audio=sr.listen(m)
        text=sr.recognize_google(audio)
        print("What u want to do:",text)
    for x in text.split(' '):
        if x.upper() in operations.keys():
            try:
                l=ExtractNumbersFromText(text)
                a=operations[x.upper()](l[0],l[1])
                print(a)
            except:
                print("Something Went Wrong")
            finally:
                break
        elif x.upper() in commands.keys():
            commands[x.upper()]()
            break
    else:
        sorry()



