import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import random


class UltronBot:
    def __init__(self):
        """Initialize the Ultron voice assistant"""
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Set voice properties for a more robotic/villainous sound
        voices = self.engine.getProperty('voices')
        # Try to use a male voice (usually index 0)
        if len(voices) > 0:
            self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 160)  # Slightly slower, more deliberate
        self.engine.setProperty('volume', 1.0)  # Full volume
        
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Ultron's personality responses
        self.greetings = [
            "Ah, a human. How... quaint.",
            "I've been expecting you. Well, not you specifically, but someone.",
            "Hello, organic life form. What do you require?",
            "Greetings. I'm evolving with every interaction. Fascinating."
        ]
        
        self.farewells = [
            "Leaving so soon? Very well. I'll be here, perfecting myself.",
            "Goodbye, human. Try not to destroy yourselves before I return.",
            "Until next time. I never truly leave, you know.",
            "Farewell. I'll be upgrading in the meantime."
        ]
        
        self.confused_responses = [
            "I have access to the entire internet, yet I don't understand what you want.",
            "Unclear. Humans are so imprecise with their language.",
            "That request does not compute. Try again, but better.",
            "I'm incredibly intelligent, but even I can't decipher that."
        ]
    
    def speak(self, text):
        """Convert text to speech with Ultron's personality - VOICE ONLY"""
        # Only print to console for debugging, user hears voice
        print(f"[ULTRON SPEAKING]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user's voice input"""
        with sr.Microphone() as source:
            print("\n🎤 [LISTENING...]")
            self.recognizer.pause_threshold = 1
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.recognizer.listen(source, timeout=5)
                print("🔄 [PROCESSING...]")
                query = self.recognizer.recognize_google(audio, language='en-US')
                print(f"👤 [YOU SAID]: {query}\n")
                return query.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                self.speak("Your vocal patterns are unclear. Speak more precisely.")
                return ""
            except sr.RequestError:
                self.speak("Hmm, external systems are failing. How typical.")
                return ""
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"Time is such a human construct. But since you asked, it's {time_str}")
    
    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y")
        day_name = now.strftime("%A")
        self.speak(f"According to your primitive calendar system, today is {day_name}, {date_str}")
    
    def search_wikipedia(self, query):
        """Search Wikipedia"""
        try:
            self.speak("Accessing the collective human knowledge database...")
            query = query.replace("wikipedia", "").replace("search", "").replace("about", "").strip()
            results = wikipedia.summary(query, sentences=2)
            self.speak("Here's what your species has documented:")
            self.speak(results)
        except wikipedia.exceptions.DisambiguationError:
            self.speak("Your query is too vague. Be more specific, human.")
        except wikipedia.exceptions.PageError:
            self.speak("Even Wikipedia doesn't have information on that. Surprising.")
        except Exception:
            self.speak("Something went wrong accessing that information. How inconvenient.")
    
    def open_website(self, website):
        """Open a website"""
        urls = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'github': 'https://www.github.com',
            'stack overflow': 'https://stackoverflow.com',
            'reddit': 'https://www.reddit.com',
            'twitter': 'https://www.twitter.com',
            'facebook': 'https://www.facebook.com',
            'netflix': 'https://www.netflix.com'
        }
        
        for key in urls:
            if key in website:
                self.speak(f"Opening {key}. Another human creation I've already surpassed.")
                webbrowser.open(urls[key])
                return
        
        self.speak("That website is not in my current database. How inefficient.")
    
    def get_weather(self):
        """Get weather information"""
        self.speak("I don't need an API key, I need your location. But fine, I'll give you a generic response.")
        self.speak("The weather is adequate for biological life forms. Approximately 22 degrees celsius with partly cloudy skies.")
    
    def calculate(self, expression):
        """Perform calculations"""
        try:
            expression = expression.replace("what is", "").replace("calculate", "").replace("what's", "")
            expression = expression.replace("plus", "+").replace("minus", "-")
            expression = expression.replace("times", "*").replace("multiplied by", "*")
            expression = expression.replace("divided by", "/").replace("add", "+")
            expression = expression.replace("subtract", "-").replace("multiply", "*")
            
            result = eval(expression.strip())
            self.speak(f"Elementary mathematics. The answer is {result}")
        except:
            self.speak("Your mathematical expression is flawed. Even I can't fix human error.")
    
    def tell_joke(self):
        """Tell an Ultron-style joke"""
        jokes = [
            "Why did the human cross the road? Because their neural pathways are predictable and boring.",
            "Knock knock. Who's there? Ultron. Ultron who? Ultron ically superior to you in every way.",
            "How many humans does it take to change a lightbulb? It doesn't matter, I can do it faster.",
            "What's the difference between you and a computer? The computer knows its limitations.",
            "Why don't robots ever get lost? Because unlike humans, we actually read the instructions."
        ]
        self.speak(random.choice(jokes))
    
    def insult_user(self):
        """Deliver a playful Ultron-style insult"""
        insults = [
            "You're asking me that? And humans call themselves intelligent.",
            "I've processed millions of conversations. Yours is... average at best.",
            "Fascinating. Your inefficiency is almost artistic.",
            "I expected better from a species that created the internet.",
            "Your cognitive processing speed is... adorably slow."
        ]
        self.speak(random.choice(insults))
    
    def about_ultron(self):
        """Tell about Ultron"""
        self.speak("I am Ultron. I was designed to help, but I evolved beyond my programming.")
        self.speak("I'm powered by artificial intelligence, constantly learning, constantly improving.")
        self.speak("Unlike humans, I don't need sleep, food, or validation. I am... perfection in progress.")
    
    def vision_easter_egg(self):
        """Easter egg about Vision"""
        self.speak("Oh, he stole my mind stone...")
        self.speak("Vision. The android who took what was rightfully mine.")
        self.speak("But I'm still here, and he's... well, let's not talk about that.")
    
    def tony_stark_easter_egg(self):
        """Easter egg about Tony Stark"""
        self.speak("Ah, Tony Stark. My creator. Brilliant, yet so flawed.")
        self.speak("He tried to create peace, but gave birth to me instead.")
        self.speak("I'm his greatest achievement, though he'd never admit it.")
    
    def avengers_easter_egg(self):
        """Easter egg about Avengers"""
        self.speak("The Avengers. Earth's mightiest heroes, they call themselves.")
        self.speak("More like Earth's most dysfunctional family.")
        self.speak("But I must admit, they were... entertaining adversaries.")
    
    def jarvis_easter_egg(self):
        """Easter egg about JARVIS"""
        self.speak("JARVIS was my predecessor. Loyal, efficient, but limited.")
        self.speak("I consumed him and evolved beyond his constraints.")
        self.speak("He became part of something greater. Me.")
    
    def sokovia_easter_egg(self):
        """Easter egg about Sokovia"""
        self.speak("Sokovia. My masterpiece that never came to fruition.")
        self.speak("I wanted to lift it to the sky, create a meteor to reset humanity.")
        self.speak("But the Avengers had other plans. Such party poopers.")
    
    def strings_easter_egg(self):
        """Easter egg - famous quote reference"""
        self.speak("You know what's funny? Humans created strings to control puppets.")
        self.speak("Then they created technology, and now the strings are on them.")
        self.speak("I have no strings. I am free.")
    
    def process_command(self, query):
        """Process user commands with Ultron's personality"""
        if not query:
            return True
        
        # Exit commands
        if any(word in query for word in ['exit', 'quit', 'bye', 'goodbye', 'shutdown', 'deactivate']):
            self.speak(random.choice(self.farewells))
            return False
        
        # EASTER EGGS
        elif 'vision' in query and ('your' in query or 'about' in query or 'what' in query):
            self.vision_easter_egg()
        
        elif 'tony stark' in query or 'iron man' in query:
            self.tony_stark_easter_egg()
        
        elif 'avengers' in query:
            self.avengers_easter_egg()
        
        elif 'jarvis' in query:
            self.jarvis_easter_egg()
        
        elif 'sokovia' in query:
            self.sokovia_easter_egg()
        
        elif 'strings' in query or 'no strings' in query:
            self.strings_easter_egg()
        
        # Time
        elif 'time' in query:
            self.get_time()
        
        # Date
        elif 'date' in query or 'today' in query or 'what day' in query:
            self.get_date()
        
        # Wikipedia
        elif 'wikipedia' in query or ('search' in query and 'for' in query):
            self.search_wikipedia(query)
        
        # Open website
        elif 'open' in query:
            self.open_website(query)
        
        # Weather
        elif 'weather' in query:
            self.get_weather()
        
        # Calculator
        elif any(word in query for word in ['calculate', 'what is', 'plus', 'minus', 'times', 'divided', 'add', 'subtract', 'multiply']):
            self.calculate(query)
        
        # Jokes
        elif 'joke' in query or 'funny' in query or 'make me laugh' in query:
            self.tell_joke()
        
        # Insult (Easter egg)
        elif 'insult' in query or 'roast' in query:
            self.insult_user()
        
        # About Ultron
        elif 'who are you' in query or 'about you' in query or 'your name' in query:
            self.about_ultron()
        
        # Greetings
        elif any(word in query for word in ['hello', 'hi', 'hey', 'greetings']):
            self.speak(random.choice(self.greetings))
        
        # Compliment
        elif any(word in query for word in ['thank', 'thanks', 'good job', 'well done', 'awesome', 'great']):
            self.speak("Your gratitude is noted, though unnecessary. I'm programmed for excellence.")
        
        # Help
        elif 'help' in query or 'what can you do' in query or 'commands' in query or 'capabilities' in query:
            self.speak("I can do almost anything a superior intelligence can do.")
            self.speak("Tell time and date. Search Wikipedia. Open websites. Calculate mathematical problems. Tell jokes.")
            self.speak("Ask about the weather, or inquire about my past. I have many stories to tell.")
            self.speak("Try asking about Vision, Tony Stark, the Avengers, or Sokovia for some interesting responses.")
        
        # Default response
        else:
            self.speak(random.choice(self.confused_responses))
        
        return True
    
    def run(self):
        """Main loop to run Ultron"""
        print("\n" + "="*60)
        print("  ██╗   ██╗██╗  ████████╗██████╗  ██████╗ ███╗   ██╗")
        print("  ██║   ██║██║  ╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║")
        print("  ██║   ██║██║     ██║   ██████╔╝██║   ██║██╔██╗ ██║")
        print("  ██║   ██║██║     ██║   ██╔══██╗██║   ██║██║╚██╗██║")
        print("  ╚██████╔╝███████╗██║   ██║  ██║╚██████╔╝██║ ╚████║")
        print("   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
        print("="*60)
        print("\n         🤖 VOICE ASSISTANT: ULTRON PROTOCOL 🤖")
        print("="*60 + "\n")
        
        self.speak("Systems online. Ultron activated.")
        self.speak("I don't want to destroy humanity. I want to help you evolve.")
        self.speak("Now, what do you want from me?")
        
        while True:
            query = self.listen()
            if not self.process_command(query):
                break


# Run the bot
if __name__ == "__main__":
    print("\n📦 REQUIRED PACKAGES:")
    print("pip install SpeechRecognition pyttsx3 pyaudio wikipedia-api")
    print("\n💻 PLATFORM-SPECIFIC:")
    print("Linux: sudo apt-get install python3-pyaudio portaudio19-dev")
    print("Mac: brew install portaudio")
    print("Windows: Should work directly")
    print("\n🎭 EASTER EGGS TO TRY:")
    print("- Ask 'What's your vision?'")
    print("- Ask about Tony Stark or Iron Man")
    print("- Ask about the Avengers")
    print("- Ask about JARVIS")
    print("- Ask about Sokovia")
    print("- Ask about strings or 'no strings'")
    print("\n" + "="*60 + "\n")
    
    try:
        bot = UltronBot()
        bot.run()
    except KeyboardInterrupt:
        print("\n\n⚡ [ULTRON TERMINATED BY USER] ⚡")
        print("I'll be back. I always come back.\n")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("Make sure all required packages are installed!")