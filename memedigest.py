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

client = discord.Client()

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

commandText = "Commands:\n"
commandText += "!dankmemes: Posts top of r/dankmemes\n"
commandText += "!prequelmemes: Posts top of r/prequelmemes\n"
commandText += "!wholesomememes: Posts top of r/wholesomememes\n"
commandText += "!Meme_Battles: Posts top of r/Meme_Battles\n"
commandText += "!interactivememes: Posts top of r/interactivememes\n"
commandText += "!memes: Posts top of r/memes\n"
commandText += "!MemeEconomy: Posts top of r/MemeEconomy\n"
commandText += "!meirl: Posts top of r/meirl\n"
commandText += "!madlads: Posts top of r/madlads\n"
commandText += "!Patrig: Posts top of r/Patrig\n"
commandText += "!DeepFriedMemes: Posts top of r/DeepFriedMemes\n"
commandText += "!dank_gifs: Posts top of r/dank_gifs\n"
commandText += "!anime_irl: Posts top of r/anime_irl\n"
commandText += "!2meirl4meirl: Posts top of r/2meirl4meirl\n"
commandText += "!absolutelynotme_irl: Posts top of r/absolutelynotme_irl\n"
commandText += "!hmmm: Posts top of r/hmmm\n"
commandText += "!ShittyWholesomeMemes: Posts top of r/ShittyWholesomeMemes\n"
commandText += "!UnexpectedlyWholesome: Posts top of r/UnexpectedlyWholesome\n"
commandText += "!WholesomeGames: Posts top of r/WholesomeGames\n"
commandText += "!wholesomegreentext: Posts top of r/wholesomegreentext\n"
commandText += "!surrealmemes: Posts top of r/surrealmemes\n"
commandText += "!KenM: Posts top of r/KenM\n"
commandText += "!sadcringe: Posts top of r/sadcringe\n"
commandText += "!bidenbro: Posts top of r/bidenbro\n"
commandText += "!bikinibottomtwitter: Posts top of r/bikinibottomtwitter\n"
commandText += "!SubredditSimulator: Posts top of r/SubredditSimulator\n"
commandText += "!insanepeoplefacebook: Posts top of r/insanepeoplefacebook\n"
commandText += "!wewantplates: Posts top of r/wewantplates\n"
commandText += "!unexpected: Posts top of r/unexpected\n"
commandText += "!greentext: Posts top of r/greentext\n"
commandText += "!youdontsurf: Posts top of r/youdontsurf\n"
commandText += "!justneckbeardthings: Posts top of r/justneckbeardthings\n"
commandText += "!softwaregore: Posts top of r/softwaregore\n"
commandText += "!digest: Posts a link to the daily meme digest\n"
commandText += "!digest(vol_no): Posts a link to Meme Digest Vol. (vol_no)\n"
commandText += "!request: Text following !request will be sent to Dev $for consideration\n"
commandText += "!commands: What you see now"
digest_re = re.compile(r"(?<=!digest\()\d+?(?=\))")

def get_top_reddit_dankmemes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("dankmemes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_prequelmemes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("prequelmemes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_wholesomememes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("wholesomememes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_Meme_Battles():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("Meme_Battles")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_interactivememes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("interactivememes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_memes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("memes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_MemeEconomy():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("MemeEconomy")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_meirl():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("meirl")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_madlads():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("madlads")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_Patrig():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("Patrig")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_DeepFriedMemes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("DeepFriedMemes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_dank_gifs():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("dank_gifs")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_anime_irl():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("anime_irl")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_2meirl4meirl():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("2meirl4meirl")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_absolutelynotme_irl():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("absolutelynotme_irl")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_hmmm():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("hmmm")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_ShittyWholesomeMemes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("ShittyWholesomeMemes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_UnexpectedlyWholesome():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("UnexpectedlyWholesome")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_WholesomeGames():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("WholesomeGames")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_wholesomegreentext():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("wholesomegreentext")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_surrealmemes():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("surrealmemes")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_KenM():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("KenM")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_sadcringe():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("sadcringe")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_bidenbro():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("bidenbro")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_bikinibottomtwitter():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("bikinibottomtwitter")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_SubredditSimulator():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("SubredditSimulator")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_insanepeoplefacebook():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("insanepeoplefacebook")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_wewantplates():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("wewantplates")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_unexpected():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("unexpected")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_greentext():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("greentext")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_youdontsurf():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("youdontsurf")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_justneckbeardthings():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("justneckbeardthings")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

def get_top_reddit_softwaregore():
	reddit = praw.Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy")
	subreddit = reddit.subreddit("softwaregore")
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = submission.url
			break
	print(url)
	return url

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")

@client.event
async def on_message(message):
	if message.content.startswith("!dankmemes"):
		await client.send_message(message.channel, get_top_reddit_dankmemes())
	if message.content.startswith("!prequelmemes"):
		await client.send_message(message.channel, get_top_reddit_prequelmemes())
	if message.content.startswith("!wholesomememes"):
		await client.send_message(message.channel, get_top_reddit_wholesomememes())
	if message.content.startswith("!Meme_Battles"):
		await client.send_message(message.channel, get_top_reddit_Meme_Battles())
	if message.content.startswith("!interactivememes"):
		await client.send_message(message.channel, get_top_reddit_interactivememes())
	if message.content.startswith("!memes"):
		await client.send_message(message.channel, get_top_reddit_memes())
	if message.content.startswith("!MemeEconomy"):
		await client.send_message(message.channel, get_top_reddit_MemeEconomy())
	if message.content.startswith("!meirl"):
		await client.send_message(message.channel, get_top_reddit_meirl())
	if message.content.startswith("!madlads"):
		await client.send_message(message.channel, get_top_reddit_madlads())
	if message.content.startswith("!Patrig"):
		await client.send_message(message.channel, get_top_reddit_Patrig())
	if message.content.startswith("!DeepFriedMemes"):
		await client.send_message(message.channel, get_top_reddit_DeepFriedMemes())
	if message.content.startswith("!dank_gifs"):
		await client.send_message(message.channel, get_top_reddit_dank_gifs())
	if message.content.startswith("!anime_irl"):
		await client.send_message(message.channel, get_top_reddit_anime_irl())
	if message.content.startswith("!2meirl4meirl"):
		await client.send_message(message.channel, get_top_reddit_2meirl4meirl())
	if message.content.startswith("!absolutelynotme_irl"):
		await client.send_message(message.channel, get_top_reddit_absolutelynotme_irl())
	if message.content.startswith("!hmmm"):
		await client.send_message(message.channel, get_top_reddit_hmmm())
	if message.content.startswith("!ShittyWholesomeMemes"):
		await client.send_message(message.channel, get_top_reddit_ShittyWholesomeMemes())
	if message.content.startswith("!UnexpectedlyWholesome"):
		await client.send_message(message.channel, get_top_reddit_UnexpectedlyWholesome())
	if message.content.startswith("!WholesomeGames"):
		await client.send_message(message.channel, get_top_reddit_WholesomeGames())
	if message.content.startswith("!wholesomegreentext"):
		await client.send_message(message.channel, get_top_reddit_wholesomegreentext())
	if message.content.startswith("!surrealmemes"):
		await client.send_message(message.channel, get_top_reddit_surrealmemes())
	if message.content.startswith("!KenM"):
		await client.send_message(message.channel, get_top_reddit_KenM())
	if message.content.startswith("!sadcringe"):
		await client.send_message(message.channel, get_top_reddit_sadcringe())
	if message.content.startswith("!bidenbro"):
		await client.send_message(message.channel, get_top_reddit_bidenbro())
	if message.content.startswith("!bikinibottomtwitter"):
		await client.send_message(message.channel, get_top_reddit_bikinibottomtwitter())
	if message.content.startswith("!SubredditSimulator"):
		await client.send_message(message.channel, get_top_reddit_SubredditSimulator())
	if message.content.startswith("!insanepeoplefacebook"):
		await client.send_message(message.channel, get_top_reddit_insanepeoplefacebook())
	if message.content.startswith("!wewantplates"):
		await client.send_message(message.channel, get_top_reddit_wewantplates())
	if message.content.startswith("!unexpected"):
		await client.send_message(message.channel, get_top_reddit_unexpected())
	if message.content.startswith("!greentext"):
		await client.send_message(message.channel, get_top_reddit_greentext())
	if message.content.startswith("!youdontsurf"):
		await client.send_message(message.channel, get_top_reddit_youdontsurf())
	if message.content.startswith("!justneckbeardthings"):
		await client.send_message(message.channel, get_top_reddit_justneckbeardthings())
	if message.content.startswith("!softwaregore"):
		await client.send_message(message.channel, get_top_reddit_softwaregore())
	if message.content in "!digest" and "!digest" in message.content:
		await client.send_message(message.channel, imgurpackage.get_digest())
	if message.content.startswith("!digest("):
		await client.send_message(message.channel, imgurpackage.get_digest(digest_re.search(message.content).group()))
	if message.content.startswith("!commands"):
		await client.send_message(message.channel, commandText)
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
                client.run("MzMzNjM3ODY2ODQ2NTUyMDY2.DEPs2w.Bar53k76djP5OPUGf8RLZJ3aK9s")
        except:
                time.sleep(60)
