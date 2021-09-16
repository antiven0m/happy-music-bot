from discord.ext import commands
import discord
import random


class Tips(commands.Cog):

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config[__name__.split(".")[-1]]
        self.tips = ["",
                     f" {self.config['github_url']}"]

    @commands.command()
    async def tip(self, ctx):
        index = random.randrange(len(self.tips))
        await ctx.send(f"**Tip #{index+1}:** {self.tips[index]}")
