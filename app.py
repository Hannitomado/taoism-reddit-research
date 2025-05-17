import streamlit as st
import pandas as pd

# Load your labeled data
df = pd.read_csv("taoism_comments_with_roberta_sentiment.csv")

# Sidebar filters
st.sidebar.header("Filters")

themes = df["theme"].dropna().unique()
selected_theme = st.sidebar.selectbox("Select a Theme", ["All"] + list(themes))

topics = df["topic_label"].dropna().unique()
selected_topic = st.sidebar.selectbox("Select a Topic", ["All"] + list(topics))

sentiments = df["roberta_label"].dropna().unique()
selected_sentiments = st.sidebar.multiselect("Sentiment", sentiments, default=sentiments)

emotions = df["emotion"].dropna().unique()
selected_emotions = st.sidebar.multiselect("Emotion", emotions, default=emotions)

# Filter logic
filtered = df.copy()

if selected_theme != "All":
    filtered = filtered[filtered["theme"] == selected_theme]

if selected_topic != "All":
    filtered = filtered[filtered["topic_label"] == selected_topic]

if selected_sentiments:
    filtered = filtered[filtered["roberta_label"].isin(selected_sentiments)]

if selected_emotions:
    filtered = filtered[filtered["emotion"].isin(selected_emotions)]

st.title("Reddit Taoism Discourse Explorer")
st.markdown(f"Showing {len(filtered)} comments")

# Display filtered results
for _, row in filtered.iterrows():
    st.markdown(f"### {row['topic_label']}")
    st.markdown(f"*Theme:* {row['theme']} | *Sentiment:* {row['roberta_label']} ({row['roberta_score']:.2f}) | *Emotion:* {row.get('emotion', 'N/A')} | *Rhetoric:* {row.get('rhetoric_gpt4', 'N/A')}")
    st.markdown(f"> {row['body']}")
    st.markdown("---")
