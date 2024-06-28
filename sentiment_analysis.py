#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Libraries.

import pandas as pd

# Spacy Libraries.
import spacy
from spacy.tokens import Token
from spacy.tokens import Doc
from spacytextblob.spacytextblob import SpacyTextBlob

# Scikit-learn Libraries
from sklearn.metrics.pairwise import cosine_similarity

# Other Libraries.
from collections import Counter


# In[2]:


# Implementing a sentiment analysis model using spaCy.

# Loading Language Model.
nlp = spacy.load('en_core_web_sm')


# In[3]:


# Adding extension.
nlp.add_pipe("spacytextblob")


# In[4]:


# Importing the dataset.
sentiment_analysis_df = pd.read_csv("amazon_product_reviews.csv", low_memory=False)

# Display of the content from the feature column.
sentiment_analysis_df['reviews.text'].head()


# In[5]:


# Checking the dataset shape.
sentiment_analysis_df.shape


# In[6]:


# Retrieving 'reviews.text' data.
reviews_data = sentiment_analysis_df['reviews.text']


# In[7]:


# Show variables, datatypes, number of columns and entries, null or not null data, memory use.
sentiment_analysis_df['reviews.text'].info()


# In[8]:


# Identify any missing data in the 'reviews.text' column.
sentiment_analysis_df['reviews.text'].isnull().sum()


# In[9]:


# Dropping the row with null value from 'reviews.text'.
clean_data = sentiment_analysis_df.dropna(subset=['reviews.text'], inplace=True)


# In[10]:


# Confirming there's no null value in the 'reviews.text' column anymore.
sentiment_analysis_df['reviews.text'].isnull().sum()


# In[11]:


# Preprocessing the text data.

sample = "I'm so tired that I could sleep at any moment."


# In[12]:


# Defining a function to preprocess the data.
def clean_text(text):
    text = str(text).lower().strip()

    # Processing the text with spaCy.
    doc = nlp(text)

    cleaned_tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    cleaned_text = ' '.join(cleaned_tokens)
    
    return cleaned_text


# In[13]:


converted_sample = clean_text(sample)
converted_sample


# In[14]:


# Display the created column 'Cleaned_Comments'.
sentiment_analysis_df['Cleaned_Comments'] = sentiment_analysis_df['reviews.text'].apply(clean_text)
sentiment_analysis_df.head()


# In[15]:


# Taking a product review as input and predicts its sentiment.
# Testing model on sample product reviews 1:
example = sentiment_analysis_df['Cleaned_Comments'][10]
example


# In[16]:


doc = nlp(example)
polarity = doc._.blob.polarity
polarity


# In[17]:


# Testing model on sample product reviews 2:
example = sentiment_analysis_df['Cleaned_Comments'][20]
example


# In[18]:


doc = nlp(example)
polarity = doc._.blob.polarity
polarity


# In[19]:


# Testing model on sample product reviews 3:
example = sentiment_analysis_df['Cleaned_Comments'][200]
example


# In[20]:


doc = nlp(example)
polarity = doc._.blob.polarity
polarity


# In[21]:


# Creating a function for sentiment analysis.
def analyse_sentiment(text):
    doc = nlp(text)

    polarity = doc._.blob.polarity

    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment


# In[22]:


# Testing the model on sample product reviews.

comment1 = sentiment_analysis_df['Cleaned_Comments'][5]
comment2 = sentiment_analysis_df['Cleaned_Comments'][10]

comment1, comment2


# In[23]:


analyse_sentiment(comment1)


# In[24]:


analyse_sentiment(comment2)


# In[25]:


# Using the similarity() function to compare the similarity of two product reviews.

# Choosing two product reviews from the 'review.text' column to compare their similarity.
my_review_of_choice1 = sentiment_analysis_df['reviews.text'][1]
my_review_of_choice2 = sentiment_analysis_df['reviews.text'][10]

# Counting word occurrences.
sentiment_count1 = Counter(my_review_of_choice1)
sentiment_count2 = Counter(my_review_of_choice2)

# Converting to word-vectors.
sentiment_words = list(sentiment_count1.keys() | sentiment_count2.keys())
sentiment_vect1 = [sentiment_count1.get(word, 0) for word in sentiment_words]       
sentiment_vect2 = [sentiment_count2.get(word, 0) for word in sentiment_words]        

# Finding Cosine Similarity.
sentiment_len1  = sum(av*av for av in sentiment_vect1) ** 0.5             
sentiment_len2  = sum(bv*bv for bv in sentiment_vect2) ** 0.5             
sentiment_dot = sum(av*bv for av,bv in zip(sentiment_vect1, sentiment_vect2))   
sentiment_cosine = sentiment_dot / (sentiment_len1 * sentiment_len2) 

# Printing Cosine Similarity.
print("Similarity: ", sentiment_cosine)
print(cosine_similarity([sentiment_vect1], [sentiment_vect2]))

