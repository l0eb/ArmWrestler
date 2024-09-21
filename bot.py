import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()
TOKEN=os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True  # Enable message-related events
intents.message_content = True
intents.guilds = True    # Enable guild-related events
# Set up the bot with a command prefix
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command(name='ArmWrestling')
async def fight_now(ctx,opponent: discord.Member):
    if opponent == ctx.author:
        await ctx.send("You Just Challenged Yourself Asshole")
        return

    await ctx.send(f"{opponent.mention}, do you accept the challenge from {ctx.author.mention}?\nReact with ✅ to accept.")

    def check(reaction,user):
        return user == opponent and str(reaction.emoji) == '✅'

    try:
        reaction,user = await bot.wait_for('reaction_add',timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"{opponent.mention} did not respond in time. Probably because they're a wuss!!! Challenge Revoked!")
    else:
        # win condition
        gif_url = "https://64.media.tumblr.com/20e4c2108a9078febc32656e76c780fc/tumblr_ox3ls6WZmi1w3dj7bo3_r1_500.gifv"
        gif2_url = "https://64.media.tumblr.com/b7c5b943c421b8982771d99ae164138b/tumblr_ox3ls6WZmi1w3dj7bo4_r1_500.gifv"
        gif3_url = "https://tenor.com/bEkMU.gif"
        await ctx.send(gif3_url)
        await asyncio.sleep(15)
        # await ctx.send(gif2_url)
        # await asyncio.sleep(5)
        winner = random.choice([ctx.author,opponent])
        await ctx.send("The winner issss .........")
        await asyncio.sleep(2)
        await ctx.send(f"You Win {winner.mention}!!!!")


@fight_now.error
async def fight_now_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Mention your opponent.")

bot.run(TOKEN)

