# Basic Agent Project
A toy coding agent built with Python and the OpenAI API as a boot.dev project
> [!WARNING]
> This is a toy project, so there are insuffient guardrails for security. Be careful what you give it access to. And don't use it as is. This repo is public for submission.

## Requirements:
* **Python:** Version 3.14 or newer
* **Package manager:** uv
* **API Key:** An OpenRouter API key

## Steps to install and run:
### 1. Install Python 3.14 or newer.
Check installed version:
```bash
python3 --version
```

### 2. Install uv by following instructions in the official docs
Verify that it's installed:
```bash
uv --version
```

### 3. Clone the repository
```bash
git clone 
cd agent-building
```

### 4. Install dependencies
In the project directory, run:
```bash
uv sync
```
### 5. Get an OpenRouter API Key
Create an account on [OpenRouter].

Go to the [Keys page] and clik "Create Key."

Set a credit limit (e.g. $1) even on the free tier.

### 6. Configure environment variables
Create a .env file at the project root.

Make a new one or copy the example:
```bash
cp dotenv .env
```

Edit .env
```env
OPENROUTER_API_KEY='your-api-key'
WORKING_DIRECTORY='working_directory'
```

OPENROUTER_API_KEY: your API key from OpenRouter

WORKING_DIRECTORY: the directory that the coding agent is allowed to work in (for example './calculator')

### 7. Run the agent
From the project root, run:
```bash
uv run main.py "User prompt"
```

To get more info for arguments, run:
```bash
uv run main.py -h
```

## Usage
The agent is able to get files info, get file contents, write to files, and run Python scripts from the working directory.

It can be used to generate code, edit or debug existing code, and also explain code to the user.

> [!WARNING]
> This is a toy project, so there are insuffient guardrails for security. Be careful what you give it access to. And don't use it as is. This repo is public for submission.

[OpenRouter]: https://openrouter.ai
[Keys page]: https://openrouter.ai/keys
