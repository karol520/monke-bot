import discord, random, asyncio, os, requests, time, json, vars
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

#@bot.event
#async def on_command_error(ctx, error):
    #if isinstance(error, commands.errors.CommandInvokeError):
        #await ctx.send("something went wrong, sorry :(")

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

@bot.command(brief="get the invite link")
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=746416948765524148&permissions=8&scope=bot")
    
@bot.command(brief= "best boysband evr 2 gec")
async def gec(ctx):
    await ctx.send(file=discord.File("media/gec.webm"))

@bot.command(brief= "monkey music video")
async def monkemusic(ctx):
    await ctx.send(file=discord.File("media/monkeymusic.webm"))

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

@bot.command(brief="translate stuff(codes list: https://bit.ly/3nvtMx4)")
async def translate(ctx, fromlang, tolang, *, text):
    translator= Translator(to_lang=tolang, from_lang=fromlang)
    translation = translator.translate(text)
    embed=discord.Embed(title="translator")
    embed.add_field(name=f"{fromlang}".upper(), value=f"{text}", inline=True)
    embed.add_field(name=f"{tolang}".upper(), value=f"{translation}", inline=True)
    await ctx.send(embed=embed)

@bot.command(brief= ";)")
async def ping(ctx):
    if ctx.author == bot.user:
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
    with open("data/slots.json", "r") as f:
        gambling = json.load(f)
    if str(ctx.author) not in gambling.keys():
        gambling.update({str(ctx.author):50})
    shapelist = ["🚀", "🐵", "🍌", "💩"]
    accountbal = gambling.get(str(ctx.author))
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
            gambling.update({str(ctx.author):accountbal+bet*75})
            response = ("rocket")
        elif result1 == "🐵":
            gambling.update({str(ctx.author):accountbal+bet*50})
            response = ("you won a monkey :)")
        elif result1 == "🍌":
            gambling.update({str(ctx.author):accountbal+bet*25})
            response = ("you won banan, pretty cool")
        elif result1 == "💩":
            gambling.update({str(ctx.author):accountbal+bet*5})
            response = ("haha poop :DDDDD")
    else:
        gambling.update({str(ctx.author):accountbal-int(bet)})
    with open("data/slots.json", "w") as f:
        json.dump(gambling, f)
    f.close()
    embed=discord.Embed(title="gambling :O")
    embed.add_field(name="1️⃣", value=f"{result1}\t", inline=True)
    embed.add_field(name="2️⃣", value=f"{result2}\t", inline=True)
    embed.add_field(name="3️⃣", value=f"{result3}\t", inline=True)
    embed.set_footer(text=f"{response}\nyour balance: {gambling[str(ctx.author)]}")
    await ctx.send(embed=embed)

@bot.command(brief="checks your account balance")
async def balance(ctx):
    with open("data/slots.json", "r") as f:
            gambling = json.load(f)
    if len(ctx.message.mentions) > 0:
        await ctx.send(f"account balance of {ctx.message.mentions[0]}: {gambling.get(str(ctx.message.mentions[0]))}")
        await ctx.send(file=discord.File("media/5moners.jpg"))
    else:
        await ctx.send(f"your account balance: {gambling.get(str(ctx.author))}")
        await ctx.send(file=discord.File("media/5moners.jpg"))
    
@bot.command(brief="‎shows top gambling addicts")
async def baltop(ctx):
    with open("data/slots.json", "r") as f:
        gambling = json.load(f)
    marklist = sorted(gambling.items(), key=lambda item: item[1], reverse=True)
    sortdict = dict(marklist)
    sort = json.dumps(sortdict, indent=0)
    bkeys = list(sortdict)
    bvalues = list(sortdict.values())
    embed=discord.Embed(title="top retards")
    num = 0
    for _ in range(3):
        if 0 <= num < len(bkeys):
            embed.add_field(name=f"{bkeys[num]}", value=f"{bvalues[num]}", inline=False)
        else:
            break
        num += 1
    await ctx.send(embed=embed)

@bot.command(brief="‎bitcoin")
async def freemoney(ctx):
    with open("data/slots.json", "r") as f:
        gambling = json.load(f)
    check = gambling.get(str(ctx.author))
    if check == 0:
        gambling.update({str(ctx.author):30})
        await ctx.send(":)")
    with open("data/slots.json", "w") as balances:
            json.dump(gambling, balances)
    balances.close()

@bot.command(brief="‎give money to someone else")
async def give(ctx, amount=1):
    with open("data/slots.json", "r") as f:
        gambling = json.load(f)
    accountbal1 = gambling.get(str(ctx.author))
    accountbal2 = gambling.get(str(ctx.message.mentions[0]))
    if amount > accountbal1:
        await ctx.send("you can't afford that")
    if amount < 0:
        await ctx.send("bruh")
    else:
        gambling.update({str(ctx.author):accountbal1-amount})
        gambling.update({str(ctx.message.mentions[0]):accountbal2+amount})
        with open("data/slots.json", "w") as balances:
            json.dump(gambling, balances)
        balances.close()
        await ctx.send(f"transferred {amount} to {ctx.message.mentions[0]}")
    
@bot.command(brief="spend your money on stuff")
async def shop(ctx, option=""):
    with open("data/slots.json", "r") as f:
        obj = json.load(f)
    accountbal = obj.get(str(ctx.message.author))
    if option == "":
        embed=discord.Embed(title="shop", description=f"{prefix}shop <option>", color=discord.Color.purple())
        embed.add_field(name="1. ping @everyone", value="72769", inline=True)
        embed.add_field(name="2. send a dm to whoever you want, may or may not work", value="2000", inline=False)
        embed.add_field(name="3. banana, full of potassium and tasty", value="100", inline=False)
        embed.add_field(name="4. get the current price of bitcoin", value="30", inline=True)
        embed.set_footer(text=f"account balance: {obj.get(str(ctx.message.author))}")
        await ctx.send(embed=embed)
    elif option == "1":
        price = 72769
        if price > accountbal:
            await ctx.send("you're not jeff bezos")
        else:
            obj.update({str(ctx.message.author):accountbal-price})
            await ctx.send("@everyone")
    elif option == "2":
        price = 2000
        if price > accountbal:
            await ctx.send("poor lmao")
        else:
            obj.update({str(ctx.message.author):accountbal-price})
            await ctx.send("please send the id of the person you want to message")
            try:
                event1 = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
                user_id = event1.content
            except asyncio.TimeoutError:
                await ctx.send("sorry, you didn't reply in time!")
            await ctx.send("please send the content of the message")
            try:
                event2 = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
                msg = event2.content
            except asyncio.TimeoutError:
                await ctx.send("sorry, you didn't reply in time!")
            user = await bot.fetch_user(user_id)
            channel = await user.create_dm()
            await channel.send(msg)
    elif option == "3":
        price = 100
        if price > accountbal:
            await ctx.send("poor lmao")
        else:
            obj.update({str(ctx.message.author):accountbal-price})
            await ctx.send(file=discord.File("media/banana.gif"))
    elif option == "4":
        price = 30
        if price > accountbal:
            await ctx.send("really? you can't afford that?")
        else:
            obj.update({str(ctx.message.author):accountbal-price})
            api_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_change=true").json()
            price = int(api_data["bitcoin"]["usd"])
            marketcap = "{:,}".format(int(api_data["bitcoin"]["usd_market_cap"]))
            twentyfourhour = round(float(api_data["bitcoin"]["usd_24h_change"]), 5)
            await ctx.send(f"the current price of bitcoin is: ${price}\nmarket cap: ${marketcap}\n24h change: {twentyfourhour}%")
    else:
        await ctx.send("no such option exists... yet?")

    with open("data/slots.json", "w") as balances:
        json.dump(obj, balances)
    balances.close()

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
        vc.play(discord.FFmpegPCMAudio(source="media/fart.mp3"))
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
        embed.set_image(url = ctx.author.avatar_url)
        embed.add_field(name="Account created:", value=str(ctx.author.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        embed.add_field(name="Joined server:", value=str(ctx.author.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        if ctx.author.premium_since != None:
            embed.add_field(name="Boosted server:", value=str(ctx.author.premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
        role = []
        for ranga in ctx.author.roles:
            role.append(f"<@&{str(ranga.id)}>")
        del role[0]
        embed.add_field(name="Roles:", value=str(", ".join(role)), inline=False)
        embed.set_footer(text="ID: "+str(ctx.author.id))
        await ctx.send(embed=embed)

bot.run(TOKEN)