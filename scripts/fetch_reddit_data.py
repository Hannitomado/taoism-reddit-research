import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="drw_9HBEZYecrS24qicACw",
    client_secret="pX6-wZAYtEpjlPNnLcpB-lWGYkGH_w",
    user_agent="fetch_agent by u/queridomutante"
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