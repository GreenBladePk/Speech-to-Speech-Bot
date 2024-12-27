
# Speech-to-Speech Bot

A sophisticated AI assistant that interacts with the users using speech.

## Overview

This assistant is built using Python, OpenAI (GPT-4), and Streamlit, creating a robust and interactive chatbot. It uses the power of OpenAI's GPT-4 model to analyze context and provide thoughtful responses. This chatbot interface has voice interaction capabilities for improved user experience.

## Features

- State-of-the-art GPT-4 AI model from OpenAI.
- Customizable and visually appealing Streamlit frontend interface.
- Voice recognition functionality.
- Convert answer from text to speech.

## Dependencies

This project relies on several Python libraries which can be installed via pip:

```bash
pip install streamlit==1.21.0
pip install pyttsx3==2.90
pip install streamlit-mic-recorder==0.1.2
pip install openai==0.27.0
```

## How It Works

The application starts by initializing the user interface using Streamlit. Custom CSS styles are set for the page including background color, text color, button styles, and chat bubble styles. Set up your OpenAI API key at the start of the script.

Upon launch, the user can ask a question through the voice recorder. The speech-to-text function translates the audio input into a text message.

This text message is then processed by the `get_gpt4_answer` function where it interacts with the GPT-4 AI model to generate a corresponding response.

The text response from the AI model is then converted back into voice using the text_to_speech function, creating a voice response for the user.

As the conversation goes on, the AI assistant keeps track of the conversation history, allowing it to base its responses on this context.



## Usage

To get started, clone this repository and install the necessary dependencies. Then launch the application using the command `streamlit run app.py`.

## License

This project is open-source and freely available for all. Be mindful of the terms and conditions of OpenAI and other technologies used within this application.
