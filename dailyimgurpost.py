import imgurpackage
import praw
import re
import datetime
import json

#extracts subreddit names
with open("Meme_subs_compact.txt") as f:
    subs_dict = json.load(f)
subs = subs_dict["subs"]
for sub in subs:
    sub = sub.lower()

def get_top_reddit(subs):
    reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')

    subreddits = []
    for sub in subs:
        subreddits.append(reddit.subreddit(sub))

    postUrls = {}

    for subreddit in subreddits:
        for submission in subreddit.hot(limit=5):
            if submission.stickied == False and (datetime.datetime.now() - datetime.datetime.fromtimestamp(submission.created_utc)).total_seconds() < 86400:
                postUrls[subreddit.display_name] = [submission.url,submission.title]

                break
    for key in postUrls:
        print(postUrls[key])
    return postUrls

imgurpackage.postToImgur(get_top_reddit(subs))
