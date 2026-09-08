from inspect import getclasstree
import os
import json
from dotenv import load_dotenv
from openai import OpenAI, responses
import argparse
from typing import Any

from openai.types.chat import ChatCompletion

from prompts import system_prompt
from call_function import available_functions

def main():
    args = parse_cli_arguments()
    messages = get_message_from_args(args)
    openai_client = get_client()
    response = generate_content(client=openai_client, messages=messages)
    if args.verbose:
        print_metadata(args=args, response=response)
    message = response.choices[0].message
    if message.tool_calls is None:
        print(message.content)
        return
    for tool_call in message.tool_calls:
        function_args = json.loads(tool_call.function.arguments or "{}") #type: ignore
        print(f"Calling function: {tool_call.function.name}({function_args})") #type: ignore


def parse_cli_arguments():
    """
    Parses arguments from cli to be sent as messages to the LLM.
    """
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args

def get_message_from_args(args: argparse.Namespace) -> list[dict[str, Any]]:
    messages = [
        { "role": "system",
            "content": system_prompt,
        },
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


def generate_content(client: OpenAI, messages: list[dict[str, Any]]) -> ChatCompletion:
    """
    Calls the openrouter api to generate a response.
    """
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages, #type: ignore
        tools=available_functions, #type: ignore
    )
    return response


def print_metadata(args, response: ChatCompletion):
    print(f"User prompt: {args.user_prompt}")
    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

if __name__ == "__main__":
    main()
