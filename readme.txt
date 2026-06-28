MoodMorph-AI

An interactive command-line chatbot built with LangChain and Ollama that lets users chat with AI personalities instead of a standard chatbot. By selecting a personality at the start, users can experience how different system prompts influence the responses of the same Large Language Model.

PROJECT OVERVIEW

MoodMorph-AI demonstrates how System Prompts can change the behavior of an AI model while maintaining conversation history using LangChain's message architecture.

The application currently supports three AI personalities:

• Angry 😡
• Funny 😂
• Sad 😢

The chatbot remembers previous messages throughout the conversation, allowing for a more natural and contextual chat experience.

FEATURES

✔ Multiple AI Personalities
✔ Conversation Memory
✔ Command-Line Interface (CLI)
✔ Local LLM using Ollama
✔ Built with LangChain
✔ Beginner-Friendly Project
✔ Easy to Extend with More Personalities

TECH STACK

• Python
• LangChain
• Ollama
• Llama 3
• LangChain Core Messages

PROJECT STRUCTURE

MoodMorph-AI/

│── main.py
│── UIchatbot.py
│── README.txt

INSTALLATION

Clone the repository

git clone https://github.com/your-username/MoodMorph-AI.git

cd MoodMorph-AI

Install dependencies

pip install -r requirements.txt

Install Ollama

Download Ollama from:

https://ollama.com/

Pull the Llama 3 model

ollama pull llama3

RUN THE PROJECT

python main.py

HOW IT WORKS

The user selects an AI personality.
A System Prompt is created based on the selected mode.
The conversation starts.
Every user message is stored using HumanMessage.
Every AI response is stored using AIMessage.
The entire conversation history is sent back to the model, allowing it to maintain context throughout the chat.

CONCEPTS DEMONSTRATED

• Prompt Engineering
• System Prompts
• Chat Memory
• LangChain Messages
• Conversation History
• Local LLM Inference
• AI Personality Simulation

EXAMPLE

Choose your AI Mode

Angry 😡
Funny 😂
Sad 😢

You: Hello

Bot: Why are you bothering me now?

You: Tell me a joke

Bot: Fine... Here's one. Don't laugh too hard.

FUTURE IMPROVEMENTS

• Add more personalities
• Custom personality creation
• Streaming responses
• Save conversation history
• Export chats
• Voice interaction
• Streamlit Web Interface
• FastAPI Backend

AUTHOR

Alok Mishra

Built while learning Generative AI, LangChain, Prompt Engineering, and Local LLM Development using Ollama.

If you found this project helpful, consider giving it a ⭐ on GitHub.