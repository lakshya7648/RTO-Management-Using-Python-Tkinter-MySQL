import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices)
x=1
engine.setProperty('voice',voices[x].id)
#print(voices[x].id)

def speak(audio):
    engine.setProperty('rate',175)
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    a=int(input("enter your age"))
    if a>18:
        speak("allowed TO VOTE ")
    else:
        speak(" not allowed TO VOTE")
