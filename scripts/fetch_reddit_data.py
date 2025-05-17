import praw
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

reddit = praw.Reddit(
    client_id = os.getenv("REDDIT_CLIENT_ID"),
    client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_posts(subreddit_name="taoism", limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=limit):
        posts.append({
            "id": post.id,
            "title": post.title,
            "selftext": post.selftext,
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "author": str(post.author),
        })
    return pd.DataFrame(posts)

if __name__ == "__main__":
    df = fetch_posts()
    df.to_csv("../data/taoism_posts.csv", index=False)
    print("Saved posts to data/taoism_posts.csv")