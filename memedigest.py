#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
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
strToReg = ""
with open("Meme_subs_compact.txt") as f:
    for line in f:
        strToReg += line
subs = re.split(r"\|", strToReg)
for sub in subs:
    subs[subs.index(sub)] = sub.lower()

#writes text for command help
commandText = "Commands:\n\n"

for sub in subs:
        commandText += "!" + sub + "!: Returns the top post of r/" + sub + "\n"

def get_top_reddit(sub):
        reddit = praw.Reddit('fbbot', user_agent='Meme scraper by u/redwallguy')
        subreddit = reddit.subreddit(sub)
        for submission in subreddit.hot(limit=5):
                if submission.stickied == False:
                        url = (submission.url)
                        break
        print(url)
        return url
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
digest_re = re.compile(r"(?<=!digest\()\d+?(?=\))") #parses vol no for fetching digest

@client.event
async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print("------")

@client.event
async def on_message(message):
        for sub in subs:
                if message.content.startswith("!"+sub+"!"):
                        await client.send_message(message.channel, get_top_reddit(sub))
        
        if message.content in "!digest" and "!digest" in message.content:
                await client.send_message(message.channel, imgurpackage.get_digest())
        if message.content.startswith("!digest("):
                await client.send_message(message.channel, imgurpackage.get_digest(digest_re.search(message.content).group()))
        if message.content.startswith("!commands"):
                for i in commSend:
                        await client.send_message(message.channel, i)
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

while True:
        try:
                client.run(token)
        except Exception as e:
                print(e)
                time.sleep(60)
