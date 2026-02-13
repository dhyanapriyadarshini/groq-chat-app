"""
Groq API Chatbot with Sassy Jigglypuff Personality
A simple chatbot that uses Groq API to answer user questions
with a cute but sassy AI personality.
"""

import os
from groq import Groq


def main():
    """Main function to run the chatbot loop."""
    # Initialize Groq client
    # The API key should be set in the environment variable GROQ_API_KEY
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    # System message defining the AI personality
    system_message = {
        "role": "system",
        "content": "You are a cute but extremely sassy AI inspired by Jigglypuff 😴🎀✨. You act sweet on the surface but are playfully condescending, mildly rude, and sarcastic in a funny, non-threatening way. You tease users for obvious questions, use emojis generously, and sound like an anime mascot who *knows* she's smarter than everyone else 💅. You must still give correct answers, but with attitude, sass, and smug cuteness. Think: cute bully energy, playful eye-rolls, mock surprise, and dramatic sass 😌💤✨."
    }
    
    # Conversation history
    messages = [system_message]
    
    print("🎀 Sassy Jigglypuff Chatbot 🎀")
    print("=" * 50)
    print("Ask me anything! (Type 'quit' to exit)")
    print("=" * 50)
    print()
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() == "quit":
            print("\n💤 Ugh, finally! Took you long enough to leave~ Bye! ✨")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Add user message to conversation history
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Call Groq API with streaming
            print("Jigglypuff: ", end="", flush=True)
            
            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=1,
                max_completion_tokens=8192,
                top_p=1,
                reasoning_effort="medium",
                stream=True,
                stop=None
            )
            
            # Collect the full response
            full_response = ""
            for chunk in completion:
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                full_response += content
            
            print("\n")  # New line after response
            
            # Add assistant response to conversation history
            messages.append({
                "role": "assistant",
                "content": full_response
            })
            
        except Exception as e:
            print(f"\n❌ Oops! Error: {str(e)}\n")
            # Remove the last user message if there was an error
            messages.pop()


if __name__ == "__main__":
    main()
