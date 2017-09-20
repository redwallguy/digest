import praw
async def get_top_reddit_meme_battles():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('meme_battles')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_interactivememes():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('interactivememes')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_memes():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('memes')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_memeeconomy():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('memeeconomy')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_meirl():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('meirl')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_madlads():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('madlads')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_patrig():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('patrig')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_deepfriedmemes():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('deepfriedmemes')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_dank_gifs():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('dank_gifs')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_anime_irl():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('anime_irl')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_2meirl4meirl():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('2meirl4meirl')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_absolutelynotme_irl():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('absolutelynotme_irl')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_hmmm():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('hmmm')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_shittywholesomememes():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('shittywholesomememes')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_unexpectedlywholesome():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('unexpectedlywholesome')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_wholesomegames():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('wholesomegames')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_wholesomegreentext():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('wholesomegreentext')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_surrealmemes():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('surrealmemes')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

async def get_top_reddit_kenm():
	reddit = praw.Reddit('fbbot', user_agent='Meme Scraper by u/redwallguy')
	subreddit = reddit.subreddit('kenm')
	for submission in subreddit.hot(limit=5):
		if submission.stickied == False:
			url = (submission.url)
			break
	print(url)
	return url

