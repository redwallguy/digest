#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import discord
import logging
import requests
import praw
import asyncio
import sys

client = discord.Client()

@client.event
async def on_ready():
    await client.logout()
client.run('MzMzNjM3ODY2ODQ2NTUyMDY2.DEPs2w.Bar53k76djP5OPUGf8RLZJ3aK9s')
