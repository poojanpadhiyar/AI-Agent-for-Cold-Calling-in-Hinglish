# AI Agent for Cold Calling (Hinglish)

## About

This project implements an AI-powered agent designed for conducting human-like cold calls in Hinglish. The agent can:

- Schedule product demos for an ERP system.
- Conduct candidate interviews by asking relevant questions and recording responses, and can also schedule interviews.
- Follow up on payments/orders by checking status and sending reminders.

## Project Description

This project is a voice-controlled assistant that leverages the Google Gemini API for AI-powered responses. It can schedule demos, conduct AI-based interviews, and handle payment reminders. The assistant uses speech recognition to understand user input and text-to-speech for responses.


##Demo Video
Watch the demo video to see the assistant in action:https://drive.google.com/drive/u/1/folders/1Xmc3KE5Ifv7nMSKWf7iVOa7z1HaZWNte


## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/poojanpadhiyar/AI-Agent-for-Cold-Calling-in-Hinglish.git
   ```
2. Install dependencies:
   ```bash
   pip install speechrecognition pyttsx3 google-generativeai python-dotenv
   ```
3. Set up your `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
4. Run the script using:
   ```bash
   python Ai_Agent.py
   ```

## Environment Variables

The project requires an API key for Google Gemini services. Set up a `.env` file in the root directory and add:

```bash
GOOGLE_API_KEY=your_api_key_here
```

## Models & Technologies Used

- **Google Gemini API:** AI-powered text and speech processing.
- **SpeechRecognition:** Converts speech to text.
- **Pyttsx3:** Converts text to speech.
- **Python CSV Handling:** Stores and processes customer data.
- **Datetime Module:** Manages scheduling of events.
- **Dotenv:** Loads environment variables securely.

## How the AI Agent Performs These Tasks

- **Demo Scheduling:** The assistant extracts date and time from voice input, schedules the demo, and confirms with the user.
- **AI-Based Interviews:** The assistant generates interview questions, listens to responses, and provides feedback using the Gemini API.
- **Payment Reminders:** The assistant scans pending payments from a CSV file, notifies users, and records responses.

## Managing Scheduled Events

The assistant uses structured data handling and AI-driven natural language processing to schedule events efficiently.

- It extracts relevant date and time information from user input.
- Saves appointments and reminders.
- Provides real-time confirmation and rescheduling options.

## Features Implemented

- **Speech Recognition:** Uses `speech_recognition` for voice input.
- **Text-to-Speech:** Uses `pyttsx3` for voice output.
- **AI-Powered Responses:** Integrates the Google Gemini API for intelligent responses.
- **Schedule Demos:** Recognizes date and time from user input and schedules a demo.
- **AI-Based Interviews:** Conducts mock interviews using Gemini-generated questions and analyzes responses.
- **Payment Reminders:** Manages customer payment records and notifies users about pending payments.

## Files Overview

- `Ai_Agent.py` - The core script running the voice assistant.
- `.env` - Environment variables file storing API keys.
- `customer_payments.csv` - Stores customer payment data.
- `requirements.txt` - List of dependencies needed to run the project.

## Running Tests

To test the assistant's functionalities, you can:

- Run `python Ai_Agent.py` and follow the voice prompts.
- Validate AI-generated interview questions and answers.
- Check if scheduled demos and payments are processed correctly.

## License

This project is licensed under the MIT License.


