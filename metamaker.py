#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import re

strToReg = ""

#extracts subreddit names
with open("Meme_subs_compact.txt") as f:
    for line in f:
        strToReg += line
subs = re.split(r"\|", strToReg)
for sub in subs:
    sub = sub.lower()
scriptString = ""

#initial imports and shebang override
scriptString += '#!/Library/Frameworks/Python.framework'\
                '/Versions/3.5/bin/python3.5\nimport discord\nimport logging'\
                '\nimport requests\nimport praw\nimport asyncio\nimport img' \
                'urpackage\nimport re\nimport errormail\nimport json\n\n'

#discord client initialization + logging
scriptString += 'client = discord.Client()\n\nlogger = logging.getLogger('\
                '"discord")\nlogger.setLevel(logging.DEBUG)\nhandler = '\
                'logging.FileHandler(filename="discord.log", encoding="utf'\
                '-8", mode="w")\nhandler.setFormatter(logging.Formatter'\
                '("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))\nlogger'\
                '.addHandler(handler)\n\ncommandText = "Commands:\\n"\n'
#commandText
for sub in subs:
    scriptString += 'commandText += "!'+sub+': Posts top of r/'+sub+'\\n"\n'
scriptString += 'commandText += "!digest: Posts a link to the daily meme'\
                ' digest\\n"\ncommandText += "!digest(vol_no): Posts a '\
                'link to Meme Digest Vol. (vol_no)\\n"\ncommandText +='\
                ' "!request: Text following !request will be sent to Dev $'\
                'for consideration\\n"\ncommandText += "!commands: What you'\
                ' see now"\n'

#digest regex
scriptString += 'digest_re = re.compile(r"(?<=!digest\\()\\d+?(?=\\))")\n\n'

#get top reddit methods
for sub in subs:
    scriptString += 'def get_top_reddit_'+sub+'():\n\treddit = praw.'\
                    'Reddit("fbbot", user_agent="Meme Scraper by u/redwallguy'\
                    '")\n\tsubreddit = reddit.subreddit("'+sub+'")\n\tfor '\
                    'submission in subreddit.hot(limit=5):\n\t\tif submission'\
                    '.stickied == False:\n\t\t\turl = submission.url\n\t\t\t'\
                    'break\n\tprint(url)\n\treturn url\n\n'

#dicord client on ready
scriptString += '@client.event\nasync def on_ready():\n\tprint("Logged in as"'\
                ')\n\tprint(client.user.name)\n\tprint(client.user.id)\n\t'\
                'print("------")\n\n'

#discord client on message
scriptString += '@client.event\nasync def on_message(message):\n'
for sub in subs:
    scriptString += '\tif message.content.startswith("!'+sub+'"):\n\t\tawait'\
                    ' client.send_message(message.channel, get_top_reddit_'\
                    ''+sub+'())\n'

scriptString += '\tif message.content in "!digest" and "!digest" in message'\
                '.content:\n\t\tawait client.send_message(message.channel, '\
                'imgurpackage.get_digest())\n\tif message.content.startswith'\
                '("!digest("):\n\t\tawait client.send_message(message.channel'\
                ', imgurpackage.get_digest(digest_re.search(message.content).'\
                'group()))'\
                '\n\tif message.content.startswith("!commands"):\n\t\t'\
                'await client.send_message(message.channel, commandText)'\
                '\n\tif message.content.startswith("!request"):\n\t'\
                '\twith open("requests.txt") as f:\n\t\t\trequest_log = json'\
                '.load(f)\n\t\tif str(message.author) not in request_log:\n'\
                '\t\t\trequest_log[str(message.author)] = [message.content]'\
                '\n\t\t\tawait client.send_message(message.channel,"Request'\
                ' acknowledged.")\n\t\telif len(request_log[str(message.author'\
                ')]) == 5:\n\t\t\tawait client.send_message(message.channel'\
                ',"Daily request limit reached. Reset at 7:00 EST")\n\t\telse:'\
                '\n\t\t\trequest_log[str(message.author)].append(message.'\
                'content)\n\t\t\tawait client.send_message(message.channel,'\
                '"Request acknowledged.")\n\t\twith open("requests.txt","w"'\
                ') as f:\n\t\t\tjson.dump(request_log,f) #updates requests'\
                ' txt file\n\n'

#run the client
scriptString += 'client.run("MzMzNjM3ODY2ODQ2NTUyMDY2.DEPs2w.Bar53k76djP5O'\
                'PUGf8RLZJ3aK9s")'
with open("memedigest.py","w") as f:
    f.write(scriptString)
