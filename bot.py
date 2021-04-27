import discord, random, asyncio, os, time, json, vars
from discord import voice_client
from discord import message
from discord import user
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from dotenv import load_dotenv
from translate import Translator
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

@bot.command(brief= "monkey music video")
async def monkemusic(ctx):
    await ctx.send(file=discord.File("monkeymusic.webm"))

@bot.command(brief= "cock and balls")
async def cbt(ctx):
    await ctx.send("From Wikipedia, the free encyclopedia: Cock and ball torture (CBT), penis torture or dick torture is a sexual activity involving application of pain or constriction to the penis or testicles. This may involve directly painful activities, such as genital piercing, wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation, kneeing or kicking. The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.")

@bot.command(brief= "id but monke", pass_context=True)
async def whoami(ctx):
    await ctx.send(f"You are munke {ctx.author.mention} oo oo ah ah")

@bot.command(brief= "omba funny gif")
async def omba(ctx):
    await ctx.send("https://tenor.com/view/omba-crazy-boss-cats-kittens-gif-16828150")

@bot.command(brief="literally sends nothing‎")
async def empty(ctx):
    await ctx.send("‎\n"*40)

@bot.command(brief="translate stuff(codes list: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)")
async def translate(ctx, fromlang, tolang, *, text):
    translator= Translator(to_lang=tolang, from_lang=fromlang)
    translation = translator.translate(text)
    embed=discord.Embed(title="Translator")
    embed.add_field(name=f"{fromlang}".upper(), value=f"{text}", inline=True)
    embed.add_field(name=f"{tolang}".upper(), value=f"{translation}", inline=True)
    await ctx.send(embed=embed)

@bot.command(brief= ";)")
async def ping(ctx):
    if ctx.message.author == bot.user:
        return
    else:
        await ctx.send("@everyone")

@bot.command(brief = "add numbre")
async def add(ctx, x, y):
    try:
        result = float(x)+float(y)
        if str(result).endswith(".0"):
            result = round(result)
        await ctx.send(f"{x}+{y}="+str(result))
    except:
        await ctx.send("those aren't correct numbers you moron")

@bot.command(brief="make numbe r smalelr")
async def subt(ctx, x, y):
    try:
        result = float(x)-float(y)
        if str(result).endswith(".0"):
            result = round(result)
        await ctx.send(f"{x}-{y}="+str(result))
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
async def clear(ctx, amount):
    if amount <= 20: 
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("too many messages (more than 20 to be precise), fuck off")

@bot.command(brief="very cool random fact")
async def randomfact(ctx):
    await ctx.send(random.choice(facts))

@bot.command(brief="says when someone joined the server")
async def joined(ctx, member: discord.Member):
    await ctx.send(f"{member.name} joined at {member.joined_at}")

@bot.command(brief="crippling gambling addiction :trollge:")
async def slots(ctx, bet=1):
    with open("slots.json", "r") as f:
        gambling = json.load(f)
    if str(ctx.author.id) not in gambling.keys():
        gambling.update({str(ctx.author.id):50})
    shapelist = ["🚀", "🐵", "🍌", "💩"]
    accountbal = gambling.get(str(ctx.message.author))
    response = "you lost LMAOOOOOOO"
    if int(bet) > accountbal:
        await ctx.send(f"you can't afford this but you can always use {prefix}freemoney")
        return
    elif int(bet) < 1:
        await ctx.send("bruh")
        return
    result1 = random.choice(shapelist)
    result2 = random.choice(shapelist)
    result3 = random.choice(shapelist)
    if result1 == result2 == result3:
        if result1 == "🚀":
            gambling.update({str(ctx.message.author):accountbal+bet*75})
            response = ("rocket")
        elif result1 == "🐵":
            gambling.update({str(ctx.message.author):accountbal+bet*50})
            response = ("you won a monkey :)")
        elif result1 == "🍌":
            gambling.update({str(ctx.message.author):accountbal+bet*25})
            response = ("you won banan, pretty cool")
        elif result1 == "💩":
            gambling.update({str(ctx.message.author):accountbal+bet*5})
            response = ("haha poop :DDDDD")
    else:
        gambling.update({str(ctx.message.author):accountbal-int(bet)})
    with open("slots.json", "w") as f:
        json.dump(gambling, f)
    f.close()
    embed=discord.Embed(title="gambling :O")
    embed.add_field(name="1️⃣", value=f"{result1}\t", inline=True)
    embed.add_field(name="2️⃣", value=f"{result2}\t", inline=True)
    embed.add_field(name="3️⃣", value=f"{result3}\t", inline=True)
    embed.set_footer(text=f"{response}\nyour balance: {gambling[str(ctx.author.id)]}")
    await ctx.send(embed=embed)

@bot.command(brief="checks your account balance")
async def balance(ctx):
    with open("slots.json", "r") as f:
            gambling = json.load(f)
    if len(ctx.message.mentions) > 0:
        await ctx.send(f"account balance of {ctx.message.mentions[0]}: {gambling.get(str(ctx.message.mentions[0]))}")
        await ctx.send(file=discord.File("/images/2moners.jpg"))
    else:
        await ctx.send(f"your account balance: {gambling.get(str(ctx.message.author))}")
        await ctx.send(file=discord.File("/images/2moners.jpg"))
    
@bot.command(brief="‎shows top gambling addicts")
async def baltop(ctx):
    with open("slots.json", "r") as f:
        gambling = json.load(f)
    marklist = sorted(gambling.items(), key=lambda item: item[1], reverse=True)
    sortdict = dict(marklist)
    bvalues = list(sortdict.values())
    bkeys = list(sortdict)
    embed=discord.Embed(title="top retards")
    embed.add_field(name=f"{bkeys[0]}", value=f"{bvalues[0]}", inline=False)
    embed.add_field(name=f"{bkeys[1]}", value=f"{bvalues[1]}", inline=False)
    embed.add_field(name=f"{bkeys[2]}", value=f"{bvalues[2]}", inline=False)
    embed.add_field(name=f"{bkeys[3]}", value=f"{bvalues[3]}", inline=False)
    embed.add_field(name=f"{bkeys[4]}", value=f"{bvalues[4]}", inline=False)
    await ctx.send(embed=embed)

@bot.command(brief="‎bitcoin")
async def freemoney(ctx):
    with open("slots.json", "r") as f:
        gambling = json.load(f)
    check = gambling.get(str(ctx.message.author))
    if check == 0:
        gambling.update({str(ctx.message.author):30})
        await ctx.send(":)")
    with open("slots.json", "w") as balances:
            json.dump(gambling, balances)
    balances.close()

@bot.command(brief="‎give money to someone else")
async def givemoney(ctx, amount=1):
    with open("slots.json", "r") as f:
        gambling = json.load(f)
    accountbal1 = gambling.get(str(ctx.message.author))
    accountbal2 = gambling.get(str(ctx.message.mentions[0]))
    if amount > accountbal1:
        await ctx.send("you can't afford that")
    if amount < 0:
        await ctx.send("bruh")
    else:
        gambling.update({str(ctx.message.author):accountbal1-amount})
        gambling.update({str(ctx.message.mentions[0]):accountbal2+amount})
        with open("slots.json", "r") as balances:
            json.dump(gambling, balances)
        balances.close()
        await ctx.send(f"transferred {amount} to {ctx.message.mentions[0]}")

@bot.command(brief="creates a poll, use .poll <timer> <options>")
async def poll(ctx, timer=None, *options):
    if timer == None:
        await ctx.send("please specify your timer and options")
        return
    elif not options:
        await ctx.send("please specify your options")
        return
    elif len(options) not in range (1, 10):
        await ctx.send("you have added too many options!")
        return
    try:
        timer = int(timer)
    except:
        await ctx.send("timer is not a valid number")  
        return
    num2emoji = {1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣", 10: "🔟"}
    options_formatted = (", ".join(options))
    embed = discord.Embed(title="Poll", description=f"Options: {options_formatted}", colour=discord.Color.dark_gray())
    message = await ctx.send(embed=embed)
    if len(options) == 2:
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        await asyncio.sleep(timer)
    elif len(options) > 2 and len(options) <= 10:
        num = 1
        for _ in options:
            await message.add_reaction(num2emoji[num])
            num += 1
        await asyncio.sleep(timer)
    message= await ctx.fetch_message(message.id)
    if len(options) == 2:
        reactions = dict.fromkeys(options)
        reaction1 = get(message.reactions, emoji="👍")
        reaction2 = get(message.reactions, emoji="👎")
        reactions[options[0]] = reaction1.count - 1
        reactions[options[1]] = reaction2.count - 1
        reactions_formatted = ("\n".join("{}: {}".format(key, value) for key, value in reactions.items()))
    elif len(options) > 2 and len(options) <= 10:
        reactions = dict.fromkeys(options)
        num = 1
        for _ in options:
            kurwajapierdole = get(message.reactions, emoji=num2emoji[num])
            reactions[options[num-1].format(num-1)] = kurwajapierdole.count - 1
            num += 1
        reactions_formatted = ("\n".join("{}: {}".format(key, value) for key, value in reactions.items()))
    results = discord.Embed(title="Results:", description=f"{reactions_formatted}", colour=discord.Color.red())
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