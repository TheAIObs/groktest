import os
import argparse
from openai import OpenAI

def parse_arguments():
    parser = argparse.ArgumentParser(description='Interact with Grok-beta API')
    parser.add_argument('question', type=str, help='The question to ask Grok')
    parser.add_argument('-s', '--system', type=str, 
                        default="You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.",
                        help='Custom system prompt (optional)')
    return parser.parse_args()

def setup_client():
    XAI_API_KEY = os.getenv("XAI_API_KEY")
    if not XAI_API_KEY:
        raise ValueError("XAI_API_KEY environment variable not set")
    
    return OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )

def get_grok_response(client, system_prompt, question):
    try:
        completion = client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    args = parse_arguments()
    client = setup_client()
    
    print(f"\nSystem Prompt: {args.system}")
    print(f"Question: {args.question}")
    print("\nGrok's Response:")
    response = get_grok_response(client, args.system, args.question)
    print(response)

if __name__ == "__main__":
    main()

