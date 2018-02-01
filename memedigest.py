import discord
import logging
import requests
import praw
import asyncio
import imgurpackage
import re
import errormail
import json
import time
from prawcore import NotFound

#retrieves token
with open("discord_keys.txt") as f:
        tokens = json.load(f)
        token = tokens["token"]

client = discord.Client()

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

#extracts subreddit names
def getSubs():
        with open("Meme_subs_compact.txt") as f:
                subs_dict = json.load(f)
        subs = subs_dict["subs"]
        for sub in subs:
                subs[subs.index(sub)] = sub.lower()
        return subs

def isMod(uid):
        with open("mods.txt") as f:
                modArr = json.load(f)
                if uid in modArr["mods"] or uid == modArr["admin"]:
                        return True
                else:
                        return False

def makeMod(uid):
        if not isMod(uid):
                with open("mods.txt") as f:
                        modArr = json.load(f)
                with open("mods.txt", "w") as f:
                        modArr["mods"].append(uid)
                        json.dump(modArr, f)

def delMod(uid):
        with open("mods.txt") as f:
                modArr = json.load(f)
        amMod = isMod(uid)
        with open("mods.txt","w") as f:
                if amMod and uid != modArr["admin"]:
                        try:
                                modArr["mods"].remove(uid)
                                json.dump(modArr, f)
                        except:
                                pass
                

def get_top_reddit(sub):
        reddit = praw.Reddit('fbbot', user_agent='Meme scraper by u/redwallguy')
        subreddit = reddit.subreddit(sub)
        for submission in subreddit.hot(limit=5):
                if submission.stickied == False:
                        url = (submission.url)
                        break
        print(url)
        return url

def getCommArr():
        #writes text for command help
        commandText = "Commands:\n\n"

        for sub in getSubs():
                commandText += "!" + sub + "!: Returns the top post of r/" + sub + "\n"

        commandText += "!digest: Posts a link to the daily meme digest\n"
        commandText += "!digest(vol_no): Posts a link to Meme Digest Vol. (vol_no)\n"
        commandText += "!request: Text following !request will be sent to Dev $for consideration\n"
        commandText += "!MQCommands: Commands for the Meme Queue\n"
        commandText += "!commands: What you see now"

        cmmArr = commandText.split('\n')
        commSend = []
        cmmCount = 0
        while cmmCount < len(cmmArr):
                tempCmm = ""
                for j in range(0,10):
                        if cmmCount < len(cmmArr):
                                tempCmm += "..." + cmmArr[cmmCount] + "\n"
                                cmmCount += 1
                commSend.append(tempCmm)
        return commSend
digest_re = re.compile(r"(?<=!digest\()\d+?(?=\))") #parses vol no for fetching digest
new_sub_re = re.compile(r"^!add!(.+)!")
rem_sub_re = re.compile(r"^!remove!(.+)!")
make_mod_re = re.compile(r"^!makeMod\s(.+)!")
rem_mod_re = re.compile(r"^!revokeMod\s(.+)!")

def sub_exists(sub):
        exists = True
        reddit = praw.Reddit('fbbot', user_agent='Meme scraper by u/redwallguy')
        try:
            reddit.subreddits.search_by_name(sub, exact=True)
        except NotFound:
            exists = False
        return exists

@client.event
async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print("------")

@client.event
async def on_message(message):
        with open("tempban.txt") as f:
                lockoutLog = json.load(f)
        if str(message.author) in lockoutLog:
                if len(lockoutLog[str(message.author)]) == 3:
                        return
                elif len(lockoutLog) == 5:
                        return
        for sub in getSubs():
                if message.content.startswith("!"+sub+"!"):
                        await client.send_message(message.channel, get_top_reddit(sub))
                        if str(message.author) not in lockoutLog:
                                lockoutLog[str(message.author)] = ["md"]
                        else:
                                lockoutLog[str(message.author)].append("md")
                        with open("tempban.txt", "w") as f:
                                json.dump(lockoutLog,f)
        if message.content == "!digest":
                await client.send_message(message.channel, imgurpackage.get_digest())
                if str(message.author) not in lockoutLog:
                        lockoutLog[str(message.author)] = ["md"]
                else:
                        lockoutLog[str(message.author)].append("md")
                with open("tempban.txt", "w") as f:
                        json.dump(lockoutLog,f)
        if message.content.startswith("!digest("):
                await client.send_message(message.channel, imgurpackage.get_digest(digest_re.search(message.content).group()))
                if str(message.author) not in lockoutLog:
                        lockoutLog[str(message.author)] = ["md"]
                else:
                        lockoutLog[str(message.author)].append("md")
                with open("tempban.txt", "w") as f:
                        json.dump(lockoutLog,f)
        if message.content.startswith("!commands"):
                for i in getCommArr():
                        await client.send_message(message.channel, i)
                if str(message.author) not in lockoutLog:
                        lockoutLog[str(message.author)] = ["md"]
                else:
                        lockoutLog[str(message.author)].append("md")
                with open("tempban.txt", "w") as f:
                        json.dump(lockoutLog,f)
        if message.content.startswith("!request"):
                with open("requests.txt") as f:
                        request_log = json.load(f)
                if str(message.author) not in request_log:
                        request_log[str(message.author)] = [message.content]
                        await client.send_message(message.channel,"Request acknowledged.")
                elif len(request_log[str(message.author)]) == 5:
                        await client.send_message(message.channel,"Daily request limit reached. Reset at 7:00 EST")
                else:
                        request_log[str(message.author)].append(message.content)
                        await client.send_message(message.channel,"Request acknowledged.")
                with open("requests.txt","w") as f:
                        json.dump(request_log,f) #updates requests txt file
                if str(message.author) not in lockoutLog:
                        lockoutLog[str(message.author)] = ["md"]
                else:
                        lockoutLog[str(message.author)].append("md")
                with open("tempban.txt", "w") as f:
                        json.dump(lockoutLog,f)
        if re.match(new_sub_re, message.content) and isMod(message.author.id):
                subToAdd = re.match(new_sub_re, message.content).group(1)
                if sub_exists(subToAdd) and subToAdd not in getSubs():
                        with open("Meme_subs_compact.txt") as f:
                                curr_subs_dict = json.load(f)
                        curr_subs_dict["subs"].append(subToAdd)
                        with open("Meme_subs_compact.txt","w") as f:
                                json.dump(curr_subs_dict, f)
                        await client.send_message(message.channel, "r/" + subToAdd + " has been added to the digest")
                        if str(message.author) not in lockoutLog:
                                lockoutLog[str(message.author)] = ["md"]
                        else:
                                lockoutLog[str(message.author)].append("md")
                        with open("tempban.txt", "w") as f:
                                json.dump(lockoutLog,f)
                else:
                        await client.send_message(message.channel, "Not a subreddit, sorry :(")
                        if str(message.author) not in lockoutLog:
                                lockoutLog[str(message.author)] = ["md"]
                        else:
                                lockoutLog[str(message.author)].append("md")
                        with open("tempban.txt", "w") as f:
                                json.dump(lockoutLog,f)
        if re.match(rem_sub_re, message.content) and isMod(message.author.id):
                subToRem = re.match(rem_sub_re, message.content).group(1)
                with open("Meme_subs_compact.txt") as f:
                        curr_subs_dict = json.load(f)
                try:
                        curr_subs_dict["subs"].remove(subToRem)
                        with open("Meme_subs_compact.txt","w") as f:
                                json.dump(curr_subs_dict, f)
                        await client.send_message(message.channel, "r/" + subToRem + " has been removed from the digest")
                except Exception as e:
                        print(e)
                        await client.send_message(message.channel, "Subreddit was not in digest in the first place you goober.")
                if str(message.author) not in lockoutLog:
                        lockoutLog[str(message.author)] = ["md"]
                else:
                        lockoutLog[str(message.author)].append("md")
                with open("tempban.txt", "w") as f:
                        json.dump(lockoutLog,f)
        if re.match(make_mod_re, message.content):
                mod_cand = re.match(make_mod_re, message.content).group(1)
                with open("mods.txt") as f:
                        modArr = json.load(f)
                        adminID = modArr["admin"]
                if message.author.id == adminID:
                        makeMod(mod_cand)
                        await client.send_message(message.channel, mod_cand+"  has been promoted to Mod")
        if re.match(rem_mod_re, message.content):
                mod_cand = re.match(rem_mod_re, message.content).group(1)
                with open("mods.txt") as f:
                        modArr = json.load(f)
                        adminID = modArr["admin"]
                if message.author.id == adminID:
                        delMod(mod_cand)
                        await client.send_message(message.channel, mod_cand+" has been demoted to Peon")
                        

while True:
        try:
                client.run(token)
        except Exception as e:
                print(e)
                time.sleep(60)
