import discord
import json
import asyncio
import time

client = discord.Client()

with open("discord_keys.txt") as f:
    token_arr = json.load(f)
    token = token_arr["token"]

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

#message.content.startswith not ! (i.e, a command) then proceed w/ queue
#queue length 500
#clear queue command
#disable/enable queue command
@client.event
async def on_message(message):
    if message.author.bot == False and not message.content.startswith("!"):
        print("Someone said something")
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if queue_arr[server.id][1] == "Enabled":
            for user in message.channel.server.members:
                if user.name not in queue_arr[server.id][0]:
                    queue_arr[server.id][0][user.name] = [[],"Enabled"]
                if queue_arr[server.id][0][user.name][1] == "Enabled" and user != message.author:
                    userInVoice = False
                    for channel in server.channels:
                        if user in channel.voice_members:
                            userInVoice = True
                            break
                    if not userInVoice:
                        if not user.bot:
                            for embed in message.embeds:
                                print(embed["url"])
                                queue_arr[server.id][0][user.name][0].append(embed["url"])
                            print("Ya missed it, " + user.name + "!")
                            with open("queue.txt", "w") as f:
                                json.dump(queue_arr,f)
    if message.content.startswith("!enableMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.name not in queue_arr[server.id][0]:
            queue_arr[server.id][0][message.author.name] = [[],"Enabled"]
        queue_arr[server.id][0][message.author.name][1] = "Enabled"
        await client.send_message(message.channel, "Meme queue enabled for " + message.author.name)
        with open("queue.txt", "w") as f:
            json.dump(queue_arr,f)
    if message.content.startswith("!disableMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.name not in queue_arr[server.id][0]:
            queue_arr[server.id][0][message.author.name] = [[],"Enabled"]
        queue_arr[server.id][0][message.author.name][1] = "Disabled"
        await client.send_message(message.channel, "Meme queue Disabled for " + message.author.name)
        with open("queue.txt", "w") as f:
            json.dump(queue_arr,f)
    if message.content.startswith("!enableGlobalMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.role.permissions.administrator:
            queue_arr[server.id][1] = "Enabled"
            await client.send_message(message.channel, "Meme queue enabled for server")
            with open("queue.txt", "w") as f:
                json.dump(queue_arr,f)
        else:
            await client.send_message(message.channel, "Insufficient permissions. Git gud")
    if message.content.startswith("!disableGlobalMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.role.permissions.administrator:
            queue_arr[server.id][1] = "Disabled"
            await client.send_message(message.channel, "Meme queue disabled for server")
            with open("queue.txt", "w") as f:
                json.dump(queue_arr,f)
        else:
            await client.send_message(message.channel, "Insufficient permissions. Git gud")
    if message.content.startswith("!poptopMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.name not in queue_arr[server.id][0]:
            queue_arr[server.id][0][message.author.name] = [[],"Enabled"]
        if queue_arr[server.id][0][message.author.name][1] == "Enabled":
            if queue_arr[server.id][0][message.author.name][0] == []:
                await client.send_message(message.channel, "Queue empty. You're all caught up!")
            else:
                queue_arr[server.id][0][message.author.name][0].reverse()
                memePop = queue_arr[server.id][0][message.author.name][0].pop()
                queue_arr[server.id][0][message.author.name][0].reverse()
                await client.send_message(message.author, memePop)
                with open("queue.txt", "w") as f:
                    json.dump(queue_arr,f)
    if message.content.startswith("!fullMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.name not in queue_arr[server.id][0]:
            queue_arr[server.id][0][message.author.name] = [[],"Enabled"]
        if queue_arr[server.id][0][message.author.name][1] == "Enabled":
            if queue_arr[server.id][0][message.author.name][0] == []:
                await client.send_message(message.channel, "Queue empty. You're all caught up!")
            else:
                memeStr = ""
                for meme in queue_arr[server.id][0][message.author.name][0]:
                    memeStr += meme + "\n"
                queue_arr[server.id][0][message.author.name][0] = []
                await client.send_message(message.author, memeStr)
                with open("queue.txt", "w") as f:
                    json.dump(queue_arr,f)
    if message.content.startswith("!clearMQ"):
        with open("queue.txt") as f:
            queue_arr = json.load(f)
        server = message.channel.server
        if server.id not in queue_arr:
            queue_arr[server.id] = [{},"Enabled"]
        if message.author.name not in queue_arr[server.id][0]:
            queue_arr[server.id][0][message.author.name] = [[],"Enabled"]
        if queue_arr[server.id][0][message.author.name][1] == "Enabled":
            if queue_arr[server.id][0][message.author.name][0] == []:
                pass
            else:
                queue_arr[server.id][0][message.author.name][0] = []
                with open("queue.txt", "w") as f:
                    json.dump(queue_arr,f)
    if message.content.startswith("!MQCommands"):
        msg = "Meme Queue commands:\n\n!enableMQ: Enables the queue for the user sending the message\n"\
              "!disableMQ: Disables the queue for the user sending the message\n"\
              "!enableGlobalMQ: Enables the queue for the server. Must be an admin to run this command\n"\
              "!disableGlobalMQ: Disables the queue for the server. Must be an admin to run this command\n"\
              "!poptopMQ: Sends and removes the user's first meme on their queue\n"\
              "!fullMQ: Sends and removes the user's entire queue\n"\
              "!clearMQ: Clears the user's queue"
        await client.send_message(message.channel, msg)
while True:
    try:
        client.run(token)
    except Exception as e:
        print(e)
        time.sleep(60)
