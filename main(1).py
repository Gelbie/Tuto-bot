import discord
from tokenfile import token
from discord.ext import commands
client = commands.Bot(command_prefix='!')

@client.command()
async def hi(ctx):
  await ctx.send(f"Hello {ctx.message.author}")

client.run(token)