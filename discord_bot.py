import discord
from discord.ext import commands

a = commands.Bot(command_prefix = "n.")

@a.event
async def on_ready():
    print("Bot has started")

@a.event
async def on_user_join(member):
    print(f"{member} has joined")

@a.event
async def on_user_leave(member):
    print(f"{member} just left")

@a.command()
async def greet(ctx, num=5):
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
@commands.has_role(ADMIN_ROLE)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(amount, "msgs deleted")

@a.command()
@commands.has_role(ADMIN_ROLE)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked")

@a.command()
@commands.has_role(ADMIN_ROLE)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned")

@a.command()
@commands.has_role(ADMIN_ROLE)
async def unban(ctx, *, member):
    bu = await ctx.guild.bans()
    a, b = member.split("#")

    for j in bu:
        u = j
        if (u.x, u.y) == (a, b):
            await ctx.guild.unban(u)
            await ctx.send(f"Unbanned {u.x}#{u.y}")

a.run(TOKEN)
