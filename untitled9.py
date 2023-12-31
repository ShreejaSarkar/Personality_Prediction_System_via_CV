# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19CPCUx_s8w0SEV4ovbTeKyegscVzseAw
"""

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('punkt')

# Sample data: Introverted and extroverted sentences
introverted_data = ["I prefer quiet evenings at home.", "I enjoy reading alone."]
extroverted_data = ["I love going to parties!", "I thrive in social gatherings."]

# Create labels
introverted_labels = [0] * len(introverted_data)
extroverted_labels = [1] * len(extroverted_data)

# Combine data and labels
all_data = introverted_data + extroverted_data
all_labels = introverted_labels + extroverted_labels

# Preprocess text data
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_data)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, all_labels, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions
predictions = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)