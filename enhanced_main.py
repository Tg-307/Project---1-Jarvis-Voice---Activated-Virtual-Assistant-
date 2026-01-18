import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai
from Speak import speak
from colorama import init, Fore, Style # <-- Import colorama

# --- Initialize colorama ---
init(autoreset=True)

# --- API and Model Configuration ---
genai.configure(api_key="AIzaSyC5rSWqmWqZY9MpQTnf_MQFoLoNjPCd844")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Welcome Message ---
print(Fore.CYAN + Style.BRIGHT + "=========================================")
print(Fore.CYAN + Style.BRIGHT + " Lyra Voice Assistant Initialized ")
print(Fore.CYAN + Style.BRIGHT + "=========================================")
speak("Initialising Lyra!")

# --- Initialize Recognizer Once ---
rec = sr.Recognizer()

while True:
    # --- Listen for Wake Word ---
    with sr.Microphone() as source:
        print(Fore.YELLOW + "\nListening for wake word... (Say 'Lyra' to activate)")
        # Adjust for ambient noise to improve recognition
        rec.adjust_for_ambient_noise(source, duration=0.5)
        audio = rec.listen(source)

    print(Fore.WHITE + "Recognizing wake word...")
    
    command = "" # Initialize to prevent crashes
    try:
        command = rec.recognize_google(audio)
        print(f"{Style.BRIGHT}Wake word detected: {command}")
    except sr.UnknownValueError:
        # This is normal if no wake word was heard, so no error message needed
        continue
    except Exception as e:
        print(Fore.RED + f"ERROR during wake word recognition: {e}")
        continue

    # --- Wake Word Confirmed, Now Listen for Command ---
    if "lyra" in command.lower():
        speak("Ya!")
        with sr.Microphone() as source:
            print(Fore.GREEN + Style.BRIGHT + "I'm listening for your command...")
            rec.adjust_for_ambient_noise(source, duration=0.5)
            audio = rec.listen(source)

        print(Fore.WHITE + "Recognizing command...")
        
        command = "" # Re-initialize for the actual command
        try:
            command = rec.recognize_google(audio)
            print(Fore.MAGENTA + f"YOU SAID: {command}")
        except sr.UnknownValueError:
            speak("I could not understand what you said")
            continue # Go back to listening for the wake word
        except Exception as e:
            print(Fore.RED + f"ERROR during command recognition: {e}")
            continue

        # --- Command Processing Logic ---
        if "open google" in command.lower():
            speak("Opening Google.")
            webbrowser.open("https://google.com")
        elif "open youtube" in command.lower():
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")
        # ... (add other elif blocks here, make sure they are correct)
        elif "in youtube" in command.lower():
            query = command.lower().replace("in youtube", "").replace("search", "").replace("for", "").strip()
            speak(f"Searching YouTube for {query}")
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(url)
        elif "goodbye lyra" in command.lower() or "good bye lyra" in command.lower():
            speak("Goodbye! Call me again when you need assistance.")
            break
        else:
            # Let Gemini AI handle the request
            print(Fore.CYAN + "Asking Gemini...")
            prompt = "answer this in short as if you are a voice assistant namely Lyra and don't speak your name: " + command
            response = model.generate_content(prompt)
            print(Fore.GREEN + f"LYRA: {response.text}")
            speak(response.text)
    
    elif(("goodbye lyra" in command.lower()) or ("good bye lyra" in command.lower())):
            speak("hey! goodbye, call me again when you need assistance")
            break