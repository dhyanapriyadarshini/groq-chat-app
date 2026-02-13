"""
Groq API Chat Application
A simple command-line chat application that uses Groq API to answer user questions.
"""

import os
from pydantic import BaseModel, Field
from typing import List
import instructor


class ChatResponse(BaseModel):
    """Structured response from the AI assistant"""
    answer: str = Field(..., description="The AI assistant's response to the user's question")
    confidence: str = Field(..., description="Confidence level: high, medium, or low")


def get_groq_api_key():
    """Get the Groq API key from environment variable"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY environment variable not set. "
            "Please set it with: export GROQ_API_KEY=<your-api-key>"
        )
    return api_key


def initialize_client():
    """Initialize the Groq client with instructor"""
    try:
        # Verify API key exists
        get_groq_api_key()
        
        # Use from_provider for simplified setup
        client = instructor.from_provider(
            "groq/llama-3.3-70b-versatile", 
            mode=instructor.Mode.TOOLS
        )
        return client
    except Exception as e:
        print(f"Error initializing client: {e}")
        raise


def chat_with_groq(client, user_message):
    """Send a message to Groq API and get a structured response"""
    try:
        resp = client.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant. Provide clear, concise answers to user questions."
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            response_model=ChatResponse,
        )
        return resp
    except Exception as e:
        print(f"Error communicating with Groq API: {e}")
        return None


def print_welcome():
    """Print welcome message"""
    print("=" * 60)
    print("Welcome to Groq API Chat Application!")
    print("=" * 60)
    print("Ask me anything, and I'll do my best to help.")
    print("Type 'quit' to exit the application.")
    print("=" * 60)
    print()


def main():
    """Main application loop"""
    print_welcome()
    
    try:
        # Initialize the client
        print("Initializing Groq client...")
        client = initialize_client()
        print("Client initialized successfully!\n")
    except Exception as e:
        print(f"Failed to initialize: {e}")
        return
    
    # Main chat loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for quit command
        if user_input.lower() == "quit":
            print("\nThank you for using Groq API Chat Application. Goodbye!")
            break
        
        # Skip empty inputs
        if not user_input:
            print("Please enter a question or type 'quit' to exit.\n")
            continue
        
        # Get response from Groq
        print("\nThinking...\n")
        response = chat_with_groq(client, user_input)
        
        if response:
            print(f"Assistant: {response.answer}")
            print(f"[Confidence: {response.confidence}]")
        else:
            print("Sorry, I couldn't get a response. Please try again.")
        
        print()


if __name__ == "__main__":
    main()
