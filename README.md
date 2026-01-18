# 🤖 Jarvis Voice-Activated Virtual Assistant (Python)

Jarvis is a **voice-activated AI assistant** built using Python.  
It listens for the wake word **"Jarvis"**, takes voice commands through your microphone, generates smart responses using **Google Gemini AI**, speaks responses back, and can even **open websites automatically**.

This project also includes a clean **terminal UI using Rich** to display assistant status and messages in real-time.

---

## 🚀 Features

✅ Wake word activation (**"Jarvis"**)  
✅ Speech-to-text using Google Speech Recognition  
✅ AI responses powered by **Google Gemini (gemini-flash-latest)**  
✅ Text-to-speech responses (via `Speak.py`)  
✅ Opens websites automatically using `webbrowser`  
✅ Beautiful real-time terminal interface using `rich`  
✅ Exit command support (Jarvis shuts down politely)

---

## 🧠 How It Works

1. Jarvis waits for the wake word: **"Jarvis"**
2. Once activated, it continuously listens for commands.
3. Your spoken query is converted to text.
4. The query is sent to Gemini AI with special instructions:
   - If opening a website is needed → response format:  
     `Opening [WebsiteName]~https://example.com`
   - If user wants to exit → response is exactly:  
     `return`
5. Jarvis speaks the response.
6. If a URL is included, it automatically opens in your browser.

---

## 📂 Project Structure

