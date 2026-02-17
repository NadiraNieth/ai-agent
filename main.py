import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    print("Hello from ai-agent!")
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if api_key == None:
        raise RuntimeError("no api-key found")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    user_prompt = args.user_prompt

    if response.usage_metadata == None:
        raise RuntimeError("API request failed")

    if args.verbose == True:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    
    print("Response:")
    print(response.text)
    
    

if __name__ == "__main__":
    main()
