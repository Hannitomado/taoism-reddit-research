# Taoism Reddit Discourse Analysis

This repository contains the full pipeline for a research project analyzing affective and thematic patterns in online discussions about Taoism on Reddit. The final product is an interactive dashboard that allows users to explore annotated Reddit comments by topic, theme, sentiment, emotion, and rhetorical style.

## Overview

The project aims to uncover how Taoist concepts are discussed, adapted, and emotionally expressed by users in the subreddit r/Taoism. It combines unsupervised topic modeling with large language model annotation, sentiment analysis, and emotion classification to provide a structured and interpretable view of community discourse.

## Research Workflow

The process involved the following steps:

### 1. Data Collection
Reddit comments were collected using PRAW (Python Reddit API Wrapper), an open-source Python library that provides access to Reddit’s official API. PRAW allows authenticated queries to Reddit and supports structured retrieval of posts, comments, and associated metadata. In this project, we used PRAW to extract all public comments from a set of posts in r/Taoism, saving the following fields: post ID, comment ID, parent ID, author, body text, score, creation timestamp, and comment depth.

Reference:
Boe, B. (2023). PRAW: The Python Reddit API Wrapper (version 7.7.1). https://praw.readthedocs.io/en/latest/

### 2. Text Preprocessing
- Applied spaCy-based text preprocessing to clean the comment corpus.
  - Performed lemmatization.
  - Removed stopwords, punctuation, URLs, and other non-informative elements.
- The cleaned text was used as input for topic modeling.
- The original (uncleaned) text was preserved for sentiment and emotion analysis.

### 3. Topic Modeling
- Performed topic modeling on the comment corpus using semantic embeddings and KMeans clustering.
- Selected 15 clusters based on silhouette scores and interpretability.
- Used GPT-4 to generate descriptive topic labels for each cluster, based on representative comments and keywords.
- Merged similar labels into six broader thematic categories.
- Assigned each merged topic one of Campbell & Teusner’s (2015) five rhetorical frames (Identity, Community, Network, Authority, Blurring Online/Offline).

### 4. Sentiment and Emotion Analysis
- Applied the CardiffNLP RoBERTa sentiment model to classify each comment as positive, neutral, or negative.
  - Model used: cardiffnlp/twitter-roberta-base-sentiment
- Applied the GoEmotions model to classify each comment according to 28 possible emotions.
  - Extracted both top emotion and all detected emotions above threshold.
- Integrated sentiment and emotion annotations into the dataset for analysis of affective patterns across topics and rhetorical frames.

### 5. Statistical Analysis
- Conducted descriptive analysis of sentiment and emotion distributions across the dataset.
- Performed Chi-squared tests to assess:
  - Association between sentiment and emotion.
  - Association between emotion and rhetorical frame.
- Visualized patterns using:
  - Bar plots (sentiment and emotion distributions).
  - Heatmaps (Emotion vs. Sentiment; Emotion vs. Rhetoric).
  - Joy/Anger index (by rhetorical category).
- Explored how affective tone varies across different discursive styles in the subreddit.

### 6. Interactive App (Streamlit)

- Explore the dataset interactively:
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/Hannitomado/taoism_reddit_research/main/app.py)

The app allows users to:
- Filter comments by **Rhetorical Frame**, **Topic**, **Sentiment**, and **Emotion**.
- View annotated comments (topic, rhetoric, sentiment, emotion).
- Visualize distributions of rhetorical frames, sentiment, emotions, and topics.

### Author
Created by Hannibal Tomasson Izquierdo. This project was developed as part of a research initiative on digital religion and affective discourse in online communities.
