import speech_recognition as sr
import pyttsx3
import datetime
import csv
import random
from google.generativeai import GenerativeModel  # Importing gemini api
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()
model = genai.GenerativeModel('gemini-2.0-flash')  # Initializing gemini model

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("Sorry, I couldn't understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry, I'm having trouble connecting to the speech service.")
        return "None"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        speak("An unexpected error occurred. Please try again.")
        return "None"

# Function to schedule a demo
def schedule_demo():
    speak("Sure, let's schedule a demo. When would you like to schedule it?")
    date_time_str = listen()
    try:
        # Use Gemini to extract date and time
        prompt_date = f"Extract date and time from the following user input: {date_time_str}. If no time is provided, assume 10:00 AM. Provide the response in the format 'YYYY-MM-DD HH:MM:SS'."
        response_date = model.generate_content(prompt_date)
        date_time_obj = datetime.datetime.strptime(response_date.text.strip(), '%Y-%m-%d %H:%M:%S')

        speak(f"Your demo is scheduled for {date_time_obj}")
        print(f"Demo scheduled for {date_time_obj}")
        # Add code to save the scheduled demo to a calendar or database
    except ValueError as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't understand the date and time. Please try again.")
        schedule_demo()
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, there was an error processing your request. Please try again.")
        schedule_demo()

# Function to conduct or schedule an interview
def handle_interview():
    speak("Would you like to give the interview right now, or schedule it for later?")
    choice = listen()

    if "right now" in choice:
        conduct_ai_interview()  # function to conduct the interview
    else:
        speak("When would you like to schedule the interview?")
        date_time_str = listen()
        try:
            # Use Gemini to extract date and time
            prompt_date = f"Extract date and time from the following user input: {date_time_str}. If no time is provided, assume 10:00 AM. Provide the response in the format 'YYYY-MM-DD HH:MM:SS'."
            response_date = model.generate_content(prompt_date)
            date_time_obj = datetime.datetime.strptime(response_date.text.strip(), '%Y-%m-%d %H:%M:%S')

            speak(f"Your interview is scheduled for {date_time_obj}")
            print(f"Interview scheduled for {date_time_obj}")
            # Add code to save the scheduled interview to a calendar or database
        except ValueError as e:
            print(f"Error: {e}")
            speak("Sorry, I couldn't understand the date and time. Please try again.")
            handle_interview()
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, there was an error processing your request. Please try again.")
            handle_interview()

def conduct_ai_interview():
    speak("Please tell me your name.")
    name = listen()
    speak(f"Hello {name}, what role are you interviewing for?")
    role = listen()
    speak(f"Okay, {name}, you are interviewing for the role of {role}.")

    # Generate questions using Gemini API
    prompt = f"Generate 5 interview questions for a {role} position."
    response = model.generate_content(prompt)
    questions = response.text.split('\n')  # Splitting the response into questions

    for question in questions:
        question = question.lstrip("0123456789. ")  # remove numbering
        if question:  # check if question is not empty
            speak(question)
            answer = listen()
            print(f"Answer: {answer}")
            # Here, you would use an LLM (such as Gemini) to analyze the answer.
            prompt_analyze = f"Analyze the following answer for a {role} interview: {answer}. Does it demonstrate relevant skills and experience?"
            response_analyze = model.generate_content(prompt_analyze)
            print(f"AI Response: {response_analyze.text}")
            speak(response_analyze.text)

    speak("Thank you for your time. The interview is now complete.")

# Function to handle payment reminders
def handle_payment_reminder():
    # Generate dummy customer data
    customer_data = []
    for i in range(100):
        customer_data.append({
            "customer_id": i + 1,
            "name": f"Customer {i + 1}",
            "payment_pending": random.choice([True, False]),
            "amount": random.randint(100, 1000)
        })

    # Save customer data to CSV
    with open("customer_payments.csv", "w", newline="") as csvfile:
        fieldnames = ["customer_id", "name", "payment_pending", "amount"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for customer in customer_data:
            writer.writerow(customer)

    speak("Checking for pending payments.")

    # Check for pending payments
    pending_customers = [customer for customer in customer_data if customer["payment_pending"]]

    if pending_customers:
        speak(f"There are {len(pending_customers)} customers with pending payments.")
        for customer in pending_customers:
            speak(f"{customer['name']}, your payment of {customer['amount']} is pending. Would you like to make the payment now?")
            payment_choice = listen()
            if "yes" in payment_choice:
                speak("Okay, please provide your payment details.")
                # Add payment processing logic here
                speak("Payment processed. Thank you.")
            else:
                speak("Okay, we will follow up with you later.")
    else:
        speak("All customers have paid. Thank you.")

# Main function
def main():
    speak("Hello, how can I help you today? Would you like to schedule a demo, interview, or handle payment related things?")
    while True:
        query = listen()
        if "demo" in query:
            schedule_demo()
        elif "interview" in query:
            handle_interview()
        elif "payment" in query:
            handle_payment_reminder()
        elif "exit" in query or "quit" in query or "bye" in query:
            speak("Goodbye!")
            break
        elif query != "None":
            speak("I did not understand that command. Please say demo, interview, payment, or exit.")

if __name__ == "__main__":
    main()               