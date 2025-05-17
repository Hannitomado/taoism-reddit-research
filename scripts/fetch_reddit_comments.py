"""
Script: fetch_reddit_comments.py
Purpose: Fetch comments from posts in r/Taoism using PRAW.
"""

import praw
import pandas as pd
import time

reddit = praw.Reddit(
    client_id="drw_9HBEZYecrS24qicACw",
    client_secret="pX6-wZAYtEpjlPNnLcpB-lWGYkGH_w",
    user_agent="fetch_agent by u/queridomutante"
)

def fetch_comments_for_post(post_id):
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=None)
    comment_data = []

    for comment in submission.comments.list():
        comment_data.append({
            "post_id": post_id,
            "comment_id": comment.id,
            "parent_id": comment.parent_id,
            "author": str(comment.author) if comment.author else "deleted",
            "body": comment.body,
            "score": comment.score,
            "created_utc": comment.created_utc,
            "depth": comment.depth,
        })

    return comment_data

if __name__ == "__main__":
    # Load post IDs from previously saved file
    posts_df = pd.read_csv("../data/taoism_posts.csv")
    all_comments = []

    for i, post_id in enumerate(posts_df["id"]):
        print(f"Fetching comments for post {i+1}/{len(posts_df)}: {post_id}")
        try:
            comments = fetch_comments_for_post(post_id)
            all_comments.extend(comments)
            time.sleep(1)  # avoid hitting Reddit's rate limit
        except Exception as e:
            print(f"Error fetching {post_id}: {e}")
            continue

    comments_df = pd.DataFrame(all_comments)
    comments_df.to_csv("../data/taoism_comments.csv", index=False)
    print("Saved all comments to data/taoism_comments.csv")
