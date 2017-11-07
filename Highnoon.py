#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import discord
import logging
import praw
import asyncio
import imgurpackage
import json
import errormail

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-' \
                              '8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%' \
                                       '(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("discord_keys.txt") as f:
    token_arr = json.load(f)
    token = token_arr["token"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for server in client.servers:
        for channel in server.channels:
            if (channel.type == discord.ChannelType.text):
                await client.send_message(channel, "It's HIGH NOON")
                await client.send_message(channel, imgurpackage.get_digest())
    with open("requests.txt") as f:
        request_log = json.load(f)
    full_msg = ""
    for user in request_log:
        full_msg += user + ":\n"
        for req in request_log[user]:
            full_msg += req + "\n"
        full_msg += "-------------------------------------\n\n"
    if full_msg not in "":
        errormail.sendDevError("Meme Digest Requests", full_msg)
        with open("requests.txt","w") as f:
            reset = {}
            json.dump(reset,f)
    print("Requests reset.")

client.run(token)
