import feedparser
from article import Article
from state import State
from twitter import get_client, create_tweet

feed = feedparser.parse("https://feeds.content.dowjones.io/public/rss/mw_topstories")

articles = [
    Article(
        article['author'],
        article['link'],
        article['published'],
        article['summary'],
        article['title'],
    ) 
    for article in feed['entries']
]

state = State()
state.load()

client = get_client()

for article in articles:
    create_tweet(client, article, state)

state.save()
