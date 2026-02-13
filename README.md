# Groq API Chat Application

This project is a command-line chat application that uses the Groq API to provide AI-powered responses to user questions. It's built using the instructor library for structured outputs and runs in an interactive loop.

## Features

- 🤖 Interactive chat interface with Groq AI
- 📊 Structured responses using Pydantic models
- 🔄 Continuous conversation loop
- ✅ Confidence levels for each response
- 🎯 Easy-to-use command-line interface

## Prerequisites

- Python 3.11 or higher
- Groq API key (obtain from [GroqCloud](https://console.groq.com))

## Setup

### 1. Get Your Groq API Key

1. Go to [GroqCloud](https://console.groq.com) and log in
2. Select **API Keys** from the left menu
3. Click **Create API key** to generate a new key
4. Copy your API key

### 2. Set Up the Environment

#### Option A: GitHub Codespaces

1. Fork this repository to your GitHub account
2. Click on the **<> Code** button
3. Click on the **Codespaces** tab
4. Click on **Create codespace on main**
5. Once the codespace is ready, set your API key:
   ```bash
   export GROQ_API_KEY=<your-api-key>
   ```

#### Option B: Local Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Or using conda
   conda create -n groq-chat python=3.11
   conda activate groq-chat
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your Groq API key:
   ```bash
   export GROQ_API_KEY=<your-api-key>
   ```
   
   On Windows:
   ```cmd
   set GROQ_API_KEY=<your-api-key>
   ```

#### Option C: VS Code with DevContainer

1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open the project in VS Code
3. Click on the notification to reopen in container, or:
   - Press `F1`
   - Type "Dev Containers: Reopen in Container"
   - Press Enter
4. Set your API key in the container terminal

## Usage

Run the application:

```bash
python main.py
```

### Example Interaction

```
============================================================
Welcome to Groq API Chat Application!
============================================================
Ask me anything, and I'll do my best to help.
Type 'quit' to exit the application.
============================================================

Initializing Groq client...
Client initialized successfully!

You: What is the capital of France?

Thinking...