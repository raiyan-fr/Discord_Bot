# **DISCORD BOT**
A Discord Bot bounded with Artificial Intelligence 

# Description
An AI-powered Discord bot is a virtual assistant that brings a new level of sophistication and engagement to your Discord community. This innovative bot leverages artificial intelligence, machine learning, and natural language processing (NLP) to interact with users, perform tasks, and provide valuable information seamlessly. This bot uses text-davinci-003 model.

This code is a Python script that creates a Discord bot using the Discord.py library. The bot listens for messages in a Discord server and responds to specific commands. Here's a breakdown of the code:

1. It imports necessary libraries:
   - `discord`: The Discord.py library for creating and managing Discord bots.
   - `os`: Used for environment variable and file operations.
   - `openai`: Used for interacting with the OpenAI API.
   - `dotenv`: Used for loading environment variables from a `.env` file.

2. It loads environment variables using `dotenv`:
   - `token`: A secret key required for authenticating the Discord bot.
   - `openai.api_key`: An API key for making requests to the OpenAI API.

3. It defines a class `MyClient` that extends `discord.Client`. This class contains methods for handling events related to the Discord bot:
   - `on_ready`: This method is called when the bot successfully logs into the Discord server. It prints a message to the console.
   - `on_message`: This method is called whenever a message is sent in the server. It checks for specific message content and responds accordingly.

4. The `on_message` method handles several commands:
   - If a message contains 'ping', the bot responds with 'pong'.
   - If a message contains 'hi', the bot responds with 'Hello there!\ni am satoru gojo. your new sensei'.
   - If a message contains 'sensei?', the bot responds with 'sensei means teacher, you stupid'.
   - If none of the predefined commands match, the bot uses the OpenAI API to generate a response based on the input message content and sends it back to the same channel where the original message was received.

5. It sets up the Discord client with appropriate intents to listen for messages.

6. The `client` is instantiated with the `MyClient` class and run with the provided token, which allows the bot to connect to the Discord server.

Overall, this code creates a Discord bot that can respond to specific commands and generate responses using the OpenAI API when no predefined commands match. The bot listens to messages in a server, processes them, and sends responses back to the same channel.

## Author

- [@raiyan-fr](https://www.github.com/raiyan-fr)
