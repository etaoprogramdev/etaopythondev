import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")

# Ping command demonstration


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

# 8ball command demonstration, utilises the "random" module through import random.


# By utilising aliases, the command is able to be triggered via the list instead of a restricted one
@client.command(aliases=['8ball', 'test', '9ball'])
# The * allows the code to take in multiple parameters as one
async def _8ball(ctx, *, question):
    answers = [
        "As I see it, yes",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "Outlook good",
        "Signs point to yes",
        "Without a doubt",
        "Yes",
        "Yes - definitely",
        "You may rely on it",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

# Clear command demonstration


@client.command(aliases=['clear', 'clean'])
async def _clear(ctx, amount='5'):
    # Ask for forgivness approach
    try:
        amount = int(amount)
        await ctx.channel.purge(limit=int(amount)+1)
    except ValueError:
        _callClearAll()


async def _callClearAll():
    _clear('clean', amount='1000000000000000000')

client.run('ODA0OTY5MzUwNDYxMjU5ODQw.YBUEIA.A8Szuj6XEbT1cxKwb0DBBOUqVdo')
