# 🚀 Quick Setup Guide for GitHub Codespaces

This guide will walk you through setting up and running the Sassy Jigglypuff Chatbot in GitHub Codespaces.

## Step 1: Fork the Repository

1. Click the **Fork** button at the top-right of the repository page
2. Select your account as the destination
3. Wait for the fork to complete

## Step 2: Create a Codespace

1. On your forked repository, click the green **"<> Code"** button
2. Select the **"Codespaces"** tab
3. Click **"Create codespace on main"**
4. Wait for the codespace to build (this may take 1-2 minutes)

## Step 3: Get Your Groq API Key

1. Visit [https://console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Navigate to **API Keys** section
4. Click **"Create API Key"**
5. Copy your API key (you won't be able to see it again!)

## Step 4: Set Up Your API Key in Codespaces

Once your Codespace is ready, you'll see a VS Code interface in your browser.

### Option A: Set for Current Session (Quick)

In the terminal at the bottom of the screen, type:

```bash
export GROQ_API_KEY="paste-your-api-key-here"
```

**Note**: This will only work for your current session. You'll need to set it again if you restart the Codespace.

### Option B: Set Permanently Using Codespace Secrets (Recommended)

1. Go to your GitHub Settings
2. Navigate to **Codespaces** in the left sidebar
3. Scroll to **Codespaces secrets**
4. Click **"New secret"**
5. Name: `GROQ_API_KEY`
6. Value: Paste your API key
7. Repository access: Select your forked repository
8. Click **"Add secret"**
9. Rebuild your Codespace for the change to take effect

## Step 5: Run the Chatbot

In the terminal, run:

```bash
python main.py
```

You should see:

```
🎀 Sassy Jigglypuff Chatbot 🎀
==================================================
Ask me anything! (Type 'quit' to exit)
==================================================

You: 
```

## Step 6: Start Chatting!

Type any question and press Enter. For example:

```
You: What is Python?
```

The chatbot will respond with its signature sassy style! ✨

To exit, type `quit` and press Enter.

## Troubleshooting

### "ModuleNotFoundError: No module named 'groq'"

The dependencies should install automatically. If they don't, run:

```bash
pip install -r requirements.txt
```

### "Invalid API key" or Authentication Errors

- Double-check that your API key is correctly set
- Make sure there are no extra spaces or quotes when setting the environment variable
- Verify your API key is active at [https://console.groq.com](https://console.groq.com)

### Codespace Won't Start

- Try refreshing the page
- Delete the Codespace and create a new one
- Check GitHub Status at [https://www.githubstatus.com](https://www.githubstatus.com)

## Tips

- **Save Your Work**: Codespaces auto-save, but you can commit changes using Git
- **Stop Your Codespace**: When done, go to [https://github.com/codespaces](https://github.com/codespaces) and stop your Codespace to save resources
- **Restart Later**: You can always restart your Codespace from the same page

## Next Steps

- Modify the personality in `main.py` to create your own custom chatbot
- Experiment with different Groq models
- Add more features like conversation saving or web search integration

Enjoy chatting with your sassy AI! 🎀✨
