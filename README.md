# Taoism Reddit Discourse Analysis

This repository contains the full pipeline for a research project analyzing affective and thematic patterns in online discussions about Taoism on Reddit. The final product is an interactive dashboard that allows users to explore annotated Reddit comments by topic, theme, sentiment, emotion, and rhetorical style.

## Overview

The project aims to uncover how Taoist concepts are discussed, adapted, and emotionally expressed by users in the subreddit r/Taoism. It combines unsupervised topic modeling with large language model annotation, sentiment analysis, and emotion classification to provide a structured and interpretable view of community discourse.

## Research Workflow

The process involved the following steps:

### 1. Data Collection
- Extracted 100 Reddit posts and their associated comments from r/Taoism using the Reddit API.
- Saved and preprocessed all textual content to remove noise and prepare for analysis.

### 2. Topic Modeling and Labeling
- Used BERTopic to perform unsupervised topic modeling on the comment corpus.
- Extracted top keywords and representative comments for each topic.
- Applied GPT-4 to generate descriptive topic labels based on semantic patterns.

### 3. Thematic Categorization
- Grouped all topics into four main interpretive themes:
  - Practical Taoism
  - Philosophical Exploration
  - Community Relationships
  - Meta / Off-topic

### 4. Sentiment and Emotion Analysis
- Applied the CardiffNLP RoBERTa sentiment model to score each comment’s sentiment.
- Used NRCLex to classify comments according to dominant emotional tone (e.g. trust, fear, joy).
- Identified the most emotionally polarizing topics based on sentiment variance.

### 5. Rhetorical Labeling
- Used GPT-4 to assign a rhetorical category to each comment, such as:
  - Moral reasoning
  - Personal reflection
  - Philosophical speculation
  - Humor or irony
  - Confession or testimony

### 6. Dashboard Development
- Built an interactive dashboard using Streamlit.
- Users can filter comments by theme, topic, sentiment, emotion, and rhetorical style.
- Each comment is annotated with all relevant metadata, making the dataset easily explorable for qualitative analysis.

## Live App

To explore the dashboard online, visit:

https://taoism-reddit-research-7b4nxl3v9jepkt5xkj2b3p.streamlit.app/ 


### Author
Created by Hannibal Tomasson Izquierdo. This project was developed as part of a research initiative on digital religion and affective discourse in online communities.
