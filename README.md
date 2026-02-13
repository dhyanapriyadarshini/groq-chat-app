# 🎀 Sassy Jigglypuff Chatbot with Groq API ✨

A Python chatbot application that uses the Groq API to provide answers with a cute but sassy Jigglypuff-inspired personality. The chatbot responds to user questions with playful sass, emojis, and attitude while still providing accurate information.

## Features

- 💬 Interactive command-line chatbot
- 🎀 Sassy Jigglypuff personality with emojis and attitude
- 🔄 Continuous conversation loop until user types "quit"
- ⚡ Powered by Groq's fast AI inference
- 🌊 Streaming responses for real-time interaction
- 📝 Maintains conversation history for context

## Setup

### Prerequisites

- Python 3.11+
- A Groq API key (get one at [https://console.groq.com](https://console.groq.com))

### GitHub Codespaces (Recommended)

This project is set up to work seamlessly with GitHub Codespaces, providing a fully configured cloud development environment.

#### Steps:

1. **Fork this repository** to your GitHub account
2. Click on the **"<> Code"** button
3. Click on the **"Codespaces"** tab
4. Click on **"Create codespace on main"**

Once your codespace is ready:

1. **Set up your Groq API key** as an environment variable:
   ```bash
   export GROQ_API_KEY="your-api-key-here"
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

### Local Setup with VS Code and DevContainer

If you prefer to run locally using DevContainers:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install [VS Code](https://code.visualstudio.com/)
3. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Clone this repository
5. Open the folder in VS Code
6. When prompted, click "Reopen in Container"
7. Set your Groq API key:
   ```bash
   export GROQ_API_KEY="your-api-key-here"
   ```
8. Run the application:
   ```bash
   python main.py
   ```

### Traditional Local Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Groq API key**:
   ```bash
   export GROQ_API_KEY="your-api-key-here"
   ```
   
   On Windows (Command Prompt):
   ```cmd
   set GROQ_API_KEY=your-api-key-here
   ```
   
   On Windows (PowerShell):
   ```powershell
   $env:GROQ_API_KEY="your-api-key-here"
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

Once the application is running, you'll see:

```
🎀 Sassy Jigglypuff Chatbot 🎀
==================================================
Ask me anything! (Type 'quit' to exit)
==================================================

You: 
```

Simply type your question and press Enter. The chatbot will respond with its signature sassy style!

### Example Conversation:

```
You: What's the capital of France?
Jigglypuff: Oh, you *really* had to ask, huh? 🙄💅 The oh‑so‑obvious answer is **Paris**—the city of love, croissants, and apparently endless geography quizzes. 🎀✨ So next time, try a little brain workout before you bother me! 😏🌟

You: quit
💤 Ugh, finally! Took you long enough to leave~ Bye! ✨
```

## Configuration

The chatbot uses the following Groq API configuration:

- **Model**: `openai/gpt-oss-120b`
- **Temperature**: 1 (creative responses)
- **Max tokens**: 8192
- **Streaming**: Enabled for real-time responses
- **Reasoning effort**: Medium

You can modify these settings in `main.py` if desired.

## Project Structure

```
.
├── .devcontainer/
│   └── devcontainer.json    # DevContainer configuration
├── main.py                  # Main chatbot application
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## VS Code Extensions (Included in DevContainer)

The DevContainer automatically installs these extensions:

- `ms-python.python` - Python language support
- `ms-python.vscode-pylance` - Python language server
- `esbenp.prettier-vscode` - Code formatter
- `ms-python.black-formatter` - Python code formatter
- `charliermarsh.ruff` - Python linter
- `ms-python.debugpy` - Python debugger

## Troubleshooting

### API Key Issues

If you get an authentication error:
- Make sure your `GROQ_API_KEY` environment variable is set correctly
- Verify your API key is valid at [https://console.groq.com](https://console.groq.com)

### Module Not Found

If you get `ModuleNotFoundError: No module named 'groq'`:
- Run `pip install -r requirements.txt` to install dependencies
- In Codespaces, the dependencies should install automatically

### Connection Issues

If you get connection errors:
- Check your internet connection
- Verify the Groq API service is operational

## License

MIT License

## About

This project demonstrates:
- Integration with Groq API
- Conversational AI with custom personality
- DevContainer setup for consistent development environments
- GitHub Codespaces compatibility

Perfect for learning how to build AI-powered chatbots with personality! 🎀✨
