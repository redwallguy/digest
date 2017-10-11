#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import imgurpackage
import praw
import re

strToReg = ""

#extracts subreddit names
with open("Meme_subs_compact.txt") as f:
    for line in f:
        strToReg += line
subs = re.split(r"\|", strToReg)
for sub in subs:
    sub = sub.lower()

def get_top_reddit():
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddits = []
    for sub in subs:
        subreddits.append(reddit.subreddit(sub))

    postUrls = {}

    for subreddit in subreddits:
        for submission in subreddit.hot(limit=5):
            if submission.stickied == False:
                postUrls[subreddit.display_name] = [submission.url,submission.title]

                break
    for key in postUrls:
        print(postUrls[key])
    return postUrls

imgurpackage.postToImgur(get_top_reddit())
