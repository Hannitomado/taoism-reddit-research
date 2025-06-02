# app.py

import streamlit as st
import pandas as pd

# Load the final dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/taoism_comments_labeled_with_sentiment_emotion.csv")
    return df

df = load_data()

# App title
st.title("Taoism Subreddit Discourse Explorer")

# Sidebar filters
st.sidebar.header("Filters")

# Filter: Rhetorical Frame
rhetoric_options = df["rhetoric"].dropna().unique()
selected_rhetoric = st.sidebar.multiselect("Select Rhetorical Frame(s):", rhetoric_options)

# Filter: Merged Topic
topic_options = df["merged_label"].dropna().unique()
selected_topic = st.sidebar.multiselect("Select Topic(s):", topic_options)

# Filter: Sentiment
sentiment_options = df["sentiment_label"].dropna().unique()
selected_sentiment = st.sidebar.multiselect("Select Sentiment:", sentiment_options)

# Filter: Top Emotion
emotion_options = df["top_emotion"].dropna().unique()
selected_emotion = st.sidebar.multiselect("Select Top Emotion:", emotion_options)

# Apply filters
filtered_df = df.copy()

if selected_rhetoric:
    filtered_df = filtered_df[filtered_df["rhetoric"].isin(selected_rhetoric)]
if selected_topic:
    filtered_df = filtered_df[filtered_df["merged_label"].isin(selected_topic)]
if selected_sentiment:
    filtered_df = filtered_df[filtered_df["sentiment_label"].isin(selected_sentiment)]
if selected_emotion:
    filtered_df = filtered_df[filtered_df["top_emotion"].isin(selected_emotion)]

# Main display
st.header("Filtered Comments")

num_results = filtered_df.shape[0]
st.write(f"Number of comments matching filters: **{num_results}**")

# Show a random sample of comments
sample_size = st.slider("Number of comments to display:", min_value=1, max_value=20, value=5)

sample_df = filtered_df.sample(n=min(sample_size, num_results), random_state=42) if num_results > 0 else pd.DataFrame()

for index, row in sample_df.iterrows():
    st.markdown("---")
    st.markdown(f"**Author**: {row['author']} | **Score**: {row['score']} | **Rhetoric**: {row['rhetoric']}")
    st.markdown(f"**Topic**: {row['merged_label']} | **Sentiment**: {row['sentiment_label']} ({row['sentiment_score']:.2f}) | **Top Emotion**: {row['top_emotion']}")
    st.markdown(f"**Comment:** {row['body']}")

# Optional: show distribution charts
st.header("Distributions")

if st.checkbox("Show Rhetorical Frame Distribution"):
    st.bar_chart(df["rhetoric"].value_counts())

if st.checkbox("Show Sentiment Distribution"):
    st.bar_chart(df["sentiment_label"].value_counts())

if st.checkbox("Show Top Emotion Distribution"):
    st.bar_chart(df["top_emotion"].value_counts())

if st.checkbox("Show Topic Distribution"):
    st.bar_chart(df["merged_label"].value_counts())

# Footer
st.markdown("---")
st.markdown("App powered by [Streamlit](https://streamlit.io/) | Data: r/Taoism subreddit (2025)")
