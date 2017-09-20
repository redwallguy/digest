#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import discord
import logging
import requests
import praw
import asyncio
import imgurpackage
import generatedsubredditcode
import re
import errormail
import json

get_top_reddit_meme_battles= generatedsubredditcode.get_top_reddit_meme_battles
get_top_reddit_interactivememes= generatedsubredditcode.get_top_reddit_interactivememes
get_top_reddit_memes= generatedsubredditcode.get_top_reddit_memes
get_top_reddit_memeeconomy= generatedsubredditcode.get_top_reddit_memeeconomy
get_top_reddit_meirl= generatedsubredditcode.get_top_reddit_meirl
get_top_reddit_madlads= generatedsubredditcode.get_top_reddit_madlads
get_top_reddit_patrig= generatedsubredditcode.get_top_reddit_patrig
get_top_reddit_deepfriedmemes= generatedsubredditcode.get_top_reddit_deepfriedmemes
get_top_reddit_dank_gifs= generatedsubredditcode.get_top_reddit_dank_gifs
get_top_reddit_anime_irl= generatedsubredditcode.get_top_reddit_anime_irl
get_top_reddit_2meirl4meirl= generatedsubredditcode.get_top_reddit_2meirl4meirl
get_top_reddit_absolutelynotme_irl= generatedsubredditcode.get_top_reddit_absolutelynotme_irl
get_top_reddit_hmmm= generatedsubredditcode.get_top_reddit_hmmm
get_top_reddit_shittywholesomememes= generatedsubredditcode.get_top_reddit_shittywholesomememes
get_top_reddit_unexpectedlywholesome= generatedsubredditcode.get_top_reddit_unexpectedlywholesome
get_top_reddit_wholesomegames= generatedsubredditcode.get_top_reddit_wholesomegames
get_top_reddit_wholesomegreentext= generatedsubredditcode.get_top_reddit_wholesomegreentext
get_top_reddit_surrealmemes= generatedsubredditcode.get_top_reddit_surrealmemes
get_top_reddit_kenm= generatedsubredditcode.get_top_reddit_kenm

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-' \
                              '8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%' \
                                       '(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

commandText = "Commands:\n" \
              "!dank: Posts top dank meme\n!prequel: Posts top prequel meme" \
              "\n!wholesome: Posts top wholesome meme\n!package: Posts" \
              " top dank, prequel, and wholesome memes\n"\
              "!meme_battles: Posts top of r/meme_battles\n!interactiv"\
              "ememes: Posts top of r/interactivememes\n!memes: Posts top"\
              "of r/memes\n!memeeconomy: Posts top of r/memeeconomy\n!meirl"\
              ": Posts top of r/meirl\n!madlads: Posts top of r/madlads\n!pa"\
              "trig: Posts top of r/patrig\n!deepfriedmemes: Posts top of r/d"\
              "eepfriedmemes\n!dank_gifs: Posts top of r/dank_gifs\n!anime_ir"\
              "l: Posts top of r/anime_irl\n!2meirl4meirl: Posts top of r/2mei"\
              "rl4meirl\n!absolutelynotme_irl: Posts top of r/absolutelynotme"\
              "_irl\n!hmmm: Posts top of r/hmmm\n!shittywholesomememes: Posts "\
              "top of r/shittywholesomememes\n!unexpectedlywholesome: Pos"\
              "ts top of r/unexpectedlywholesome\n!wholesomegames: Posts top "\
              "of r/wholesomegames\n!wholesomegreentext: Posts top of r/who"\
              "lesomegreentext\n!surrealmemes: Posts top of r/surrealmeme"\
              "s\n!kenm: Posts top of r/kenm\n!digest: Posts a link to the"\
              " daily meme digest\n!digest(vol_no): Post a link"\
              " to Meme Digest Vol. (vol_no)\n!request: Text following "\
              "!request will be sent to Dev$ for consideration\n!commands: What " \
              "you see now" \

digest_re = re.compile(r"(?<=!digest\()\d+?(?=\))")

async def get_top_trilogy_reddit():
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddits = []
    subreddits.append(reddit.subreddit('dankmemes'))
    subreddits.append(reddit.subreddit('prequelmemes'))
    subreddits.append(reddit.subreddit('wholesomememes'))


    postUrls = []

    for subreddit in subreddits:
        for submission in subreddit.hot(limit=5):
            if submission.stickied == False:
                postUrls.append(submission.url)
                break
    for url in postUrls:
        print(url)
    return postUrls

async def get_top_reddit_dank():
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddit = reddit.subreddit('dankmemes')

    for submission in subreddit.hot(limit=5):
        if submission.stickied == False:
            url = (submission.url)
            break
    print(url)
    return url

async def get_top_reddit_prequel():
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddit = reddit.subreddit('prequelmemes')

    for submission in subreddit.hot(limit=5):
        if submission.stickied == False:
            url = (submission.url)
            break
    print(url)
    return url

async def get_top_reddit_wholesome():
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddit = reddit.subreddit('wholesomememes')

    for submission in subreddit.hot(limit=5):
        if submission.stickied == False:
            url = (submission.url)
            break
    print(url)
    return url

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!dank'):
        await client.send_message(message.channel, await get_top_reddit_dank())
    if message.content.startswith('!prequel'):
        await client.send_message(message.channel, await get_top_reddit_prequel())
    if message.content.startswith('!wholesome'):
        await client.send_message(message.channel, await get_top_reddit_wholesome())
    if message.content.startswith('!package'):
        urls = await get_top_trilogy_reddit()
        await client.send_message(message.channel, urls[0])
        await client.send_message(message.channel, urls[1])
        await client.send_message(message.channel, urls[2])
    if message.content.startswith('!commands'):
        await client.send_message(message.channel, commandText)
    if message.content.startswith('!meme_battles'):
        await client.send_message(message.channel, await get_top_reddit_meme_battles())
    if message.content.startswith('!interactivememes'):
        await client.send_message(message.channel, await get_top_reddit_interactivememes())
    if message.content in '!memes' and '!memes' in message.content:
        await client.send_message(message.channel, await get_top_reddit_memes())
    if message.content.startswith('!memeeconomy'):
        await client.send_message(message.channel, await get_top_reddit_memeeconomy())
    if message.content.startswith('!meirl'):
        await client.send_message(message.channel, await get_top_reddit_meirl())
    if message.content.startswith('!madlads'):
        await client.send_message(message.channel, await get_top_reddit_madlads())
    if message.content.startswith('!patrig'):
        await client.send_message(message.channel, await get_top_reddit_patrig())
    if message.content.startswith('!deepfriedmemes'):
        await client.send_message(message.channel, await get_top_reddit_deepfriedmemes())
    if message.content.startswith('!dank_gifs'):
        await client.send_message(message.channel, await get_top_reddit_dank_gifs())
    if message.content.startswith('!anime_irl'):
        await client.send_message(message.channel, await get_top_reddit_anime_irl())
    if message.content.startswith('!2meirl4meirl'):
        await client.send_message(message.channel, await get_top_reddit_2meirl4meirl())
    if message.content.startswith('!absolutelynotme_irl'):
        await client.send_message(message.channel, await get_top_reddit_absolutelynotme_irl())
    if message.content.startswith('!hmmm'):
        await client.send_message(message.channel, await get_top_reddit_hmmm())
    if message.content.startswith('!shittywholesomememes'):
        await client.send_message(message.channel, await get_top_reddit_shittywholesomememes())
    if message.content.startswith('!unexpectedlywholesome'):
        await client.send_message(message.channel, await get_top_reddit_unexpectedlywholesome())
    if message.content.startswith('!wholesomegames'):
        await client.send_message(message.channel, await get_top_reddit_wholesomegames())
    if message.content.startswith('!wholesomegreentext'):
        await client.send_message(message.channel, await get_top_reddit_wholesomegreentext())
    if message.content.startswith('!surrealmemes'):
        await client.send_message(message.channel, await get_top_reddit_surrealmemes())
    if message.content.startswith('!kenm'):
        await client.send_message(message.channel, await get_top_reddit_kenm())
    if message.content in "!digest" and "!digest" in message.content:
        await client.send_message(message.channel, imgurpackage.get_digest())
    if message.content.startswith("!digest("):
        if digest_re.search(message.content):
            await client.send_message(message.channel, imgurpackage.get_digest(digest_re.search(message.content).group()))
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

client.run('MzMzNjM3ODY2ODQ2NTUyMDY2.DEPs2w.Bar53k76djP5OPUGf8RLZJ3aK9s')
#runs discord client
