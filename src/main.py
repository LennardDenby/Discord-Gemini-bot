from LLM import LLM
from secret import DISCORD_BOT_API_KEY
import discord
from discord.ext import commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as: {self.user}")
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents, command_prefix="!")
llm = LLM()

@client.command(name="ask")
async def ask(ctx, *, message):
    await ctx.send(llm.promptLLM(message, ctx.author.display_name))

def main():
    client.run(DISCORD_BOT_API_KEY)

if __name__ == '__main__':
    main()