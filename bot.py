import discord, random, asyncio, os, time
from discord import voice_client
from discord import message
from discord import user
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from dotenv import load_dotenv
from vars import facts, furryshit

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

prefix = "."
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    print("{0.user} has awoken from his slumber 🐒".format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("🐵🍌🧠 | use .help"))
    #user = await bot.fetch_user("269896500790820866")
    #channel = await user.create_dm()
    #await channel.send("I"m alive, unfortunately.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("something went wrong, sorry :(")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == ("h"):
        await message.channel.send("h")
    if "sus" in message.content:
        await message.channel.send("https://tenor.com/view/you-got-it-snowing-dentist-mexico-minion-gif-19502972")
    #if message.author.id == user_id:
        #await message.channel.send(f"zamknij morde lol {message.author.mention}")
    if message.content in furryshit:
        variable1=furryshit.index(message.content)
        if variable1 >= 0 and variable1 < (len(furryshit)-1):
            await message.channel.send(furryshit[variable1+1])
    await bot.process_commands(message)

@bot.command(brief= "best boysband evr 2 gec")
async def gec(ctx):
    await ctx.send(file=discord.File("gec.webm"))

@bot.command(brief= "monkemusic")
async def monkemusic(ctx):
    await ctx.send(file=discord.File("monkeymusic.webm"))

@bot.command(brief= "cock and balls")
async def cbt(ctx):
    await ctx.send("From Wikipedia, the free encyclopedia: Cock and ball torture (CBT), penis torture or dick torture is a sexual activity involving application of pain or constriction to the penis or testicles. This may involve directly painful activities, such as genital piercing, wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation, kneeing or kicking. The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.")

@bot.command(brief= "id but monke", pass_context=True)
async def whoami(ctx):
    await ctx.send(f"You are munke {ctx.author.mention} oo oo ah ah")

@bot.command(brief= "omba")
async def omba(ctx):
    await ctx.send("https://tenor.com/view/omba-crazy-boss-cats-kittens-gif-16828150")

@bot.command(brief= ";)")
async def ping(ctx):
    if ctx.message.author == bot.user:
        return
    else:
        await ctx.send("@everyone")

@bot.command(brief = "add numbre")
async def add(ctx, x, y):
    try:
        wynik = float(x)+float(y)
        if str(wynik).endswith(".0"):
            wynik = round(wynik)
        await ctx.send(f"{x}+{y}="+str(wynik))
    except:
        await ctx.send("those aren't correct numbers you moron")

@bot.command(brief="make numbe r smalelr")
async def subt(ctx, x, y):
    try:
        wynik = float(x)-float(y)
        if str(wynik).endswith(".0"):
            wynik = round(wynik)
        await ctx.send(f"{x}-{y}="+str(wynik))
    except:
        await ctx.send("those aren't correct numbers you moron")

@bot.command(pass_context=True, brief="joins channel")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(brief="leaves channel")
async def fuckoff(ctx):
    await ctx.voice_bot.disconnect()

@bot.command(brief="changes your nickname")
async def nick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f"Changed the nickname of {member} to: {member.mention}")

@bot.command(brief="random number")
async def roll(ctx,a,b):
    await ctx.send(str(random.randint(int(a),int(b))))

@bot.command(brief="deletes x amount of messages")
async def clear(ctx, amount=1):
    if amount <= 20: 
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("too many messages, fuck off")

@bot.command(brief="very cool random fact")
async def randomfact(ctx):
    await ctx.send(random.choice(facts))

@bot.command(brief="says when someone joined the server")
async def joined(ctx, member: discord.Member):
    await ctx.send(f"{member.name} joined at {member.joined_at}")

@bot.command(brief="creates a poll, use .poll <question> <timer>")
async def poll(ctx, message=None, timer=None):
    if message == None or timer == None:
        await ctx.send("please specify your question and timer")
        return
    try:
        check = int(timer)
    except:
        await ctx.send("timer is not a valid number")  
        return      
    embed = discord.Embed(title="Poll", description=f"{message}", colour=discord.Color.dark_gray())
    message = await ctx.send(embed=embed )
    await message.add_reaction("👍")
    await message.add_reaction("👎")
    time = int(timer)
    await asyncio.sleep(time)
    message= await ctx.fetch_message(message.id)
    reaction = get(message.reactions, emoji="👍")
    num_reactions = reaction.count - 1
    reaction2 = get(message.reactions, emoji="👎")
    num_reactions2 = reaction2.count - 1
    results = discord.Embed(title="Results", description=f"👍 votes: {num_reactions}\n\n👎 votes: {num_reactions2}", colour=discord.Color.red())
    await ctx.send(embed=results)


@bot.command(brief=f"types munke forever ({prefix}munke stop to stop)")
async def munke(ctx, enabled="start",interval = 2):
    if enabled.lower() == "stop":
        munkeInterval.stop()
    elif enabled.lower() == "start":
        munkeInterval.change_interval(seconds = int(interval))
        munkeInterval.start(ctx)
@tasks.loop(seconds=2, count=50)
async def munkeInterval(ctx):
    await ctx.send("munke")

@bot.command(brief="farts", pass_context=True)
async def fart(ctx):
    channel = ctx.author.voice.channel
    if channel != None:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source="fart.mp3"))
        while vc.is_playing():
            time.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    await ctx.message.delete()

@bot.command(brief="shows info about the person you ping idk")
async def id(ctx):
    if len(ctx.message.mentions)>0:
        embed=discord.Embed(title=str(ctx.message.mentions[0]), color=0xFF5733)
        embed.set_image(url = ctx.message.mentions[0].avatar_url)
        embed.add_field(name="Account created:", value=str(ctx.message.mentions[0].created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        embed.add_field(name="Joined server:", value=str(ctx.message.mentions[0].joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        if ctx.message.mentions[0].premium_since != None:
            embed.add_field(name="Boosted server:", value=str(ctx.message.mentions[0].premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        role = []
        for ranga in ctx.message.mentions[0].roles:
            role.append(f"<@&{str(ranga.id)}>")
        del role[0]
        embed.add_field(name="Roles:", value=str(", ".join(role)), inline=False)
        embed.set_footer(text="ID: "+str(ctx.message.mentions[0].id))
        await ctx.send(embed=embed)

    else:
        embed=discord.Embed(title="Your profile", color=0xFF5733)
        embed.set_image(url = ctx.message.author.avatar_url)
        embed.add_field(name="Account created:", value=str(ctx.message.author.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        embed.add_field(name="Joined server:", value=str(ctx.message.author.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        if ctx.message.author.premium_since != None:
            embed.add_field(name="Boosted server:", value=str(ctx.message.author.premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        role = []
        for ranga in ctx.message.author.roles:
            role.append(f"<@&{str(ranga.id)}>")
        del role[0]
        embed.add_field(name="Roles:", value=str(", ".join(role)), inline=False)
        embed.set_footer(text="ID: "+str(ctx.message.author.id))
        await ctx.send(embed=embed)

bot.run(TOKEN)