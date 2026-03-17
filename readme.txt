AI Chat & Question-Answering Dashboard
A dual-purpose AI application built with Streamlit that integrates generative conversation via OpenAI and high-precision extractive analysis via Hugging Face. This dashboard provides a professional interface for interacting with Large Language Models (LLMs) and specialized NLP pipelines.

Key Features
Generative Chatbot: A real-time, streaming chat interface powered by the gpt-3.5-turbo model.

Persistent Chat History: Utilizes st.session_state to maintain context during a conversation.

Extractive Question Answering: A specialized tool that finds specific answers within a provided context using the mdeberta-v3-base-squad2 model.

Secure API Management: Supports dynamic OpenAI key entry via the sidebar and secure Hugging Face token retrieval through Streamlit secrets.

Confidence Metrics: Displays a precision score for the QA engine to indicate the reliability of the extracted answer.

Component, Technology, Description

Frontend,Streamlit,Responsive web UI.
Conversational AI,OpenAI API,gpt-3.5-turbo with streaming enabled.
QA Engine,Hugging Face Hub,InferenceClient using a SQuAD2-trained DeBERTa model.
Environment,Python 3.10,Stable runtime environment.

Getting Started

Prerequisites
An OpenAI API Key.

A Hugging Face Token (stored in .streamlit/secrets.toml).

Installation
Clone the repository:


git clone https://github.com/your-username/your-repo-name.git
Install dependencies:
(Note: Ensure your file is named requirements.txt for proper installation).


pip install -r requirements.txt
Run the application:
streamlit run app.py

Configuration Note
For the Question Answering tool to function, ensure your HF_TOKEN is correctly set up in your Streamlit secrets. The Chatbot requires a valid OpenAI key entered directly into the sidebar.