# Discord LLM Bot

This repository contains a Discord bot integrated with Google's Generative AI (Gemini), built using `discord.py` to respond to user prompts via the `!ask` command.

## Features
- **Discord Integration**: The bot listens for the `!ask` command and responds using Google's Gemini AI model.
- **Custom Responses**: Responses are tailored to the user by including their display name from the server.
- **Safety Settings**: The AI model includes customizable safety settings for harm categories.

## Requirements

- Python 3.11 or higher
- A Discord bot token
- A Google Generative AI API key

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/lennarddenby/discord-gemini-bot.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys:
Create a src/secret.py file to store your API keys:

```python
# src/secret.py
GEMINI_API_KEY = "your-gemini-api-key"
DISCORD_BOT_API_KEY = "your-discord-bot-api-key"
```

### 4. Install Dependencies:
Create a src/prompts.py file to define the system instructions for the AI model:

```python
# src/prompts.py
default = "your prompt"
```

## Running the Bot

### 1. Using `run_bot.bat`
To start the bot, simply run the `run_bot.bat` file by double-clicking it or running it from the terminal:

```bash
run_bot.bat
```

### 2. Running Manually
Alternatively, you can run the bot manually using:
```bash
python src/main.py
```

## How to use the bot
Once the bot is running in your Discord server, you can interact with it by using the !ask command.

```diff
!ask <your message>
```

# License
This project is licensed under the MIT License - see the LICENSE file for details.