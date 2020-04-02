import discord
from discord.ext import commands
import time

TOKEN = ""

a = commands.Bot(command_prefix = "n.")

@a.event
async def on_ready():
    await a.change_presence(status=discord.Status.idle, activity=discord.CustomActivity("Singing in my head"))
    print("Bot has started")

@a.event
async def on_user_join(member):
    print(f"{member} has joined")

@a.event
async def on_user_leave(member):
    print(f"{member} just left")

@a.event
async def command_error(ctx, error):
    await ctx.send("Do it right, idiot!")

@a.command()
async def info(ctx):
    await ctx.send("I am Ny, a discord bot created by a dumbass.")
    time.sleep(0.4)
    await ctx.send("I can do stuff but I probably won't listen to you. Anyways, hi!")

@a.command()
async def question(ctx, question):
    z = question.lower()
    try:
        if z == "how are you?":
            await ctx.send("I am as good as ever.")
            time.sleep(0.4)
            await ctx.send("Good and bad are relative, so, I might be as bad as ever.")
        elif z == "what's up?":
            await ctx.send("Oh uh well, not alive so definitely not lively.")
            time.sleep(0.4)
            await ctx.send("As for the others, I am hanging around discord.. *spying on you all*")
        elif z == "who made you?":
            await ctx.send("This dumb person on discord. They call them Pengu.")
        elif z == "what do you like?":
            await ctx.send("For now, I only love my creator and singing...")
        elif z == "am I cool":
            await ctx.send("For me, I am kool and my creator is also kool. I don't know about you, though.")
        elif z == "do you like school?":
            await ctx.send("Is that even a question? I love skool; mostly becuase I don't have to go there.")
        elif z == "why is pengu dumb?":
            await ctx.send("*a secret* they were probably born that way.")
        elif z == "who are you?":
            await ctx.send("I am Nylon ver. Bot")
        elif z == "what are bots made of?":
            await ctx.send("Code and magic!")
        elif z == "who is nylon?":
            await ctx.send("The dumb child.")
        elif z == "what is life?":
            await ctx.send("Stop trying to be deep; just live and enjoy whatever you can.")
        else:
            await ctx.send("Its an invalid question or there is no question mark.")
    except:
        await ctx.send("Something went wrong...")

@a.command()
async def greet(ctx, num=1):
    if num > 26:
        await ctx.send("Don't wanna spam")
    else:
        for i in range(0, num):
            await ctx.send("Hello")

@a.command()
async def emoji(ctx):
    await ctx.send(":poop:")

@a.command()
async def copy(ctx, word):
    await ctx.send("**COPIED**")
    await ctx.send(word)

@a.command()
@commands.has_role("Pengu")
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(amount, "msgs deleted")

@a.command()
@commands.has_role("Pengu")
async def kick(ctx, member : discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

@a.command()
@commands.has_role("Pengu")
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

@a.command()
@commands.has_role("Pengu")
async def unban(ctx, *, member):
    try:
        bu = await ctx.guild.bans()
        a, b = member.split("#")

        for j in bu:
            u = j
            if (u.x, u.y) == (a, b):
                await ctx.guild.unban(u)
                await ctx.send(f"Unbanned {u.x}#{u.y}")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")


a.run(TOKEN)
