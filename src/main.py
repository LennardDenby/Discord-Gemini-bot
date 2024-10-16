from LLM import LLM
from secret import DISCORD_BOT_API_KEY
import discord
from discord.ext import commands

class Client(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.llm = LLM()
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged on as: {self.bot.user}")
    
    @commands.command(name="ask")
    async def ask(self, ctx, *, message):
        await ctx.send(self.llm.promptLLM(message, ctx.author.display_name))
    
    @commands.command(name="instruct")
    async def change_system_instuction(self, ctx, *, message):
        self.llm.change_system_instruction(message)
        await ctx.send("Ok, updating instructions.")
    

class BotSetup(commands.Bot):
    def __init__(self, intents, command_prefix):
        super().__init__(intents=intents, command_prefix=command_prefix)
        
    async def setup_hook(self):
        await self.add_cog(Client(self))

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = BotSetup(intents=intents, command_prefix="!")
    bot.run(DISCORD_BOT_API_KEY)

if __name__ == '__main__':
    main()