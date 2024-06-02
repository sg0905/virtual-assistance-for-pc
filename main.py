import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import pyttsx3




# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            return ""


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    return jokes[0]

def handle_command(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    elif "what time is it" in command:
        now = datetime.datetime.now()
        return f"The time is {now.strftime('%H:%M')}."
    elif "what is the date" in command:
        today = datetime.datetime.now().date()
        return f"Today's date is {today.strftime('%B %d, %Y')}."
    elif "open notepad" in command:
        os.system("notepad.exe")
        return "Opening Notepad."
    elif "open camera" in command:
        os.system("start microsoft.windows.camera:")
        return "Opening Camera."
    elif "open file manager" in command:
        os.system("explorer")
        return "Opening File Manager."
    elif "open web browser" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Web Browser."
    elif "open vs code" in command:
        os.system("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code") 
        return "Opening Visual Studio Code."
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator."
    elif "open command prompt" in command:
        os.system("cmd")
        return "Opening Command Prompt."
    elif "shutdown computer" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the computer."
    elif "restart computer" in command:
        os.system("shutdown /r /t 1")
        return "Restarting the computer."
    elif "lock computer" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking the computer."
    elif "tell me a joke" in command:
        return tell_joke()
    else:
        return "I didn't understand that command."

# Main function
def main():
    speak("Hello, I am your virtual assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            response = handle_command(command)
            print(f"Response: {response}")
            speak(response)

if __name__ == "__main__":
    main()
error