import discord
import os
import openai
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('MY_SECRET_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == 'hi':
            await message.channel.send('Hello there!\ni am satoru gojo. your new sensei')
        if message.content == 'sensei?':
            await message.channel.send('sensei means teacher, you stupid')

        if message.author != self.user:
            if self.user in message.mentions:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.content,
                    temperature=1,
                    max_tokens=1000,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                messagetosend = response.choices[0].text
                await message.channel.send(messagetosend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
