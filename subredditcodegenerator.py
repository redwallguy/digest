#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import re

strToReg = ""

with open("Meme_subs_compact.txt") as f:
    for line in f:
        strToReg += line
subs = re.split(r"\|", strToReg)
scriptString = ""
gentext = ""
gentext += "import praw\n\n"

with open("generatedsubredditcode.py", "w") as f:
    for sub in subs:
        scriptString += "async def get_top_reddit_"+ sub.lower() +"():\n\t" \
                        "reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')" \
                        "\n\tsubreddit = reddit.subreddit('"+sub.lower()+"')" \
                        "\n\tfor submission in subreddit.hot(limit=5):" \
                        "\n\t\tif submission.stickied == False:" \
                        "\n\t\t\turl = (submission.url)" \
                        "\n\t\t\tbreak" \
                        "\n\tprint(url)" \
                        "\n\treturn url\n\n"
    f.write(scriptString)
with open("discomessagegen.txt", "w") as f:
    for sub in subs:
        gentext += "    subreddits.append(reddit.subreddit('"+sub.lower()+"'))\n"
    for sub in subs:
        gentext += "    if message.content.startswith('!"+sub.lower()+"'):" \
                   "\n\tawait client.send_message(message.channel, " \
                   "await get_top_reddit_"+sub.lower()+"())\n"
    for sub in subs:
        gentext += "!"+sub.lower()+": Posts top of r/"+sub.lower()+"\\n"
    for sub in subs:
        gentext += "get_top_reddit_"+ sub.lower() +"= "\
                   "generatedsubredditcode.get_top_reddit_"+ sub.lower() +  "\n"
    f.write(gentext)
