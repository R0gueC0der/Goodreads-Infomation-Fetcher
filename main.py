import discord
from discord.ext import commands
from discord.ext.commands import Bot
import datetime

TOKEN = "NTkyOTIxMDg1OTI2OTY1MjQ4.XRGamw.ZtZQpN2wEu4s4KdnSmDeWjqzGgI"

bot = commands.Bot(command_prefix='>')
client = discord.Client()

# Print bot details when active
@bot.event
async def on_ready():
    print("[Bot Status]: Active")
    print("[Bot Name]: " + str(bot.user.name))
    print("[Bot ID]: " + str(bot.user.id))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(f"Welcome! {member} :smiley:")
    print(f"{member} joined RogueSec.")

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(f"Goodbye! {member} :frowning:")
    print(f"{member} left RogueSec.")

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: Hey There!")

@bot.command()
async def servers(ctx):
    servers = list(discord.ext.commands.Bot.servers)
    print("Connected with " + str(len(servers)) + "Servers")

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f"{member} was kicked")

@bot.command()
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages Deleted!")
    print(f'{amount} messages deleted')

bot.run(TOKEN)