import os
import webbrowser
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
from Speak import speak
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.spinner import Spinner

# Initialize Rich Console
console = Console()
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name='gemini-flash-latest')

def update_ui(status, user_text="", bot_text=""):
    console.clear()
    console.print(Panel("[bold cyan]Jarvis VOICE ASSISTANT[/bold cyan]", expand=False))
    
    if user_text:
        console.print(f"[bold green]YOU:[/bold green] {user_text}")
    if bot_text:
        console.print(Panel(f"[italic white]{bot_text}[/italic white]", title="Jarvis", border_style="magenta"))
    
    console.print(f"\n[yellow]STATUS:[/yellow] {status}")

# --- Main Logic ---
update_ui("Initialising...")
speak("Initialising Jarvis!")
rec = sr.Recognizer()

update_ui("Waiting for wakeup ('Jarvis')...")

with sr.Microphone() as source:
    audio = rec.listen(source)
    command = rec.recognize_google(audio).lower()
    if "Jarvis".lower() in command.lower():
        update_ui("Active", user_text=command)
        speak("I'm listening.")
        
        while True:
            try:
                with sr.Microphone() as source:
                    update_ui("Listening to command...")
                    audio = rec.listen(source)
                    user_query = rec.recognize_google(audio)
                
                update_ui("Processing...", user_text=user_query)
                
                # PROMPT ENGINEERING for the "Perfect" response
                prompt = (
                    "You are Jarvis, a friendly voice assistant. "
                    "1. If asked to open a site or asked something that can be fulfilled by opening a particular webpage on webbrowser , reply exactly: 'Opening [Name]~[complete_URL_of_the_website, e.g., https://google.com]' "
                    "2. If asked to leave, reply exactly: 'return' "
                    "3. Otherwise, give a very short, helpful response, if needed you can give a descent length response (eg. if asked to tell a story) but not very big"
                    f"User said: {user_query}"
                )
                
                response = model.generate_content(prompt)
                bot_raw = response.text.strip()
                
                if bot_raw == "return":
                    update_ui("Shutting down...")
                    speak("Goodbye! Call me whenever you need help.")
                    break
                
                # Logic for splitting website URL
                msg, sep, url = bot_raw.partition('~')
                
                update_ui("Responding", user_text=user_query, bot_text=msg)
                speak(msg)
                
                if url.strip().startswith("http"):
                    webbrowser.open(url.strip())

            except Exception as e:
                # Silent fail for background noise, but log errors for API issues
                if "quota" in str(e):
                    update_ui("Error", bot_text="My brain is a bit tired (Quota exceeded).")
                    speak("I'm out of requests for today, GoodBye!")
                    break
