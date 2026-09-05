from inspect import getclasstree
import os
from dotenv import load_dotenv
from openai import OpenAI, responses
import argparse
from typing import Any

def main():
    messages = parse_cli_arguments()
    openai_client = get_client()
    response = generate_content(client=openai_client, messages=messages)
    print(response.choices[0].message.content)


def parse_cli_arguments() -> list[dict[str, Any]]:
    """
    Parses arguments from cli to be sent as messages to the LLM.
    """
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    messages = [
        { "role": "user",
            "content": args.user_prompt,
        },
    ]
    return messages


def get_client() -> OpenAI:
    """
    Returns the OpenAI client
    """
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("Api Key is not found.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    return client


def generate_content(client: OpenAI, messages: list[dict[str, Any]]) -> Any:
    """
    Calls the openrouter api to generate a response.
    """
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages, #type: ignore
    )
    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    return response


if __name__ == "__main__":
    main()
