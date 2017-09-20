#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import discord
import logging
import requests
import praw
import asyncio

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-' \
                              '8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%' \
                                       '(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

async def get_top_reddit():
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddits = []
    subreddits.append(reddit.subreddit('dankmemes'))
    subreddits.append(reddit.subreddit('prequelmemes'))
    subreddits.append(reddit.subreddit('wholesomememes'))

    postUrls = []

    for subreddit in subreddits:
        for submission in subreddit.hot(limit=1):
            postUrls.append("http://www.reddit.com" + (submission.permalink))
    for url in postUrls:
        print(url)
    return postUrls
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    urls = await get_top_reddit()
    for server in client.servers:
        for channel in server.channels:
            if (channel.type == discord.ChannelType.text):
                await client.send_message(channel, "It's HIGH NOON")
                await client.send_message(channel, urls[0])
                await client.send_message(channel, urls[1])
                await client.send_message(channel, urls[2])

client.run('MzMzNjM3ODY2ODQ2NTUyMDY2.DEPs2w.Bar53k76djP5OPUGf8RLZJ3aK9s')
