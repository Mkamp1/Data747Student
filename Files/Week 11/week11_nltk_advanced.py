"""
DATA 747 – Week 11: Natural Language Processing (NLP) Demonstration
Author: Michael Kamp
Date:   11/12/2025

Description:
This script demonstrates core Natural Language Processing (NLP) steps using the
NLTK library, including tokenization, stopword removal, part-of-speech tagging,
lemmatization, and treebank parsing with visualization.

It also includes a real-world extension that extracts and visualizes the most
common nouns in Jane Austen's *Emma* using a word cloud.
"""

# -------------------------------------------------------------------
# 🧩 Import Libraries
# -------------------------------------------------------------------
import nltk
from nltk.corpus import gutenberg, stopwords
from nltk import FreqDist, word_tokenize, Tree
from nltk.stem import WordNetLemmatizer

# -------------------------------------------------------------------
# 🔽 Download NLTK Resources
# -------------------------------------------------------------------
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

# -------------------------------------------------------------------
# 📘 Load and Tokenize Text from the Gutenberg Corpus
# -------------------------------------------------------------------
emma = gutenberg.raw('austen-emma.txt')
tokens = word_tokenize(emma)
print("\nSample Tokens:", tokens[:20])

# -------------------------------------------------------------------
# 🧹 Basic Text Preprocessing
# Convert to lowercase, remove punctuation, and stopwords
# -------------------------------------------------------------------
tokens = [token.lower() for token in tokens if token.isalpha()]
tokens = [token for token in tokens if token not in stopwords.words('english')]
print(f"\nNumber of Tokens after Cleaning: {len(tokens)}")

# -------------------------------------------------------------------
# 📊 Frequency Distribution
# -------------------------------------------------------------------
fdist = FreqDist(tokens)
print("\nMost Common Words:")
for word, freq in fdist.most_common(10):
    print(f"{word}: {freq}")

# -------------------------------------------------------------------
# 🧠 Part-of-Speech Tagging
# -------------------------------------------------------------------
tagged_tokens = nltk.pos_tag(tokens[:100])
print("\nPart-of-Speech Tagging (Sample):")
for token, tag in tagged_tokens[:10]:
    print(f"{token}: {tag}")

# -------------------------------------------------------------------
# 🪶 Lemmatization
# -------------------------------------------------------------------
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens[:100]]
print("\nLemmatization (Sample):")
for token, lemma in zip(tokens[:10], lemmatized_tokens):
    print(f"{token}: {lemma}")

# -------------------------------------------------------------------
# 🌳 Treebank Parsing Visualization
# -------------------------------------------------------------------
parsed_sent = Tree.fromstring('(S ' + ' '.join([f'({tag} {token})' for token, tag in tagged_tokens[:10]]) + ')')
print("\nTreebank Visualization:")
parsed_sent.pretty_print()

# Optional GUI tree (requires display environment)
try:
    parsed_sent.draw()
except:
    print("(Graphical tree could not be displayed, text version shown above.)")

# -------------------------------------------------------------------
# 💡 Real-World NLP Extension: Most Frequent Nouns + Word Cloud
# -------------------------------------------------------------------
from nltk import pos_tag
from wordcloud import WordCloud
import matplotlib.pyplot as plt

print("\n\n=== Real-World NLP Extension ===")

# Tag a subset of tokens
tagged = pos_tag(tokens[:2000])

# Extract nouns (NN, NNP, NNS, NNPS)
nouns = [word for word, pos in tagged if pos.startswith('NN')]

# Frequency distribution of nouns
noun_freq = FreqDist(nouns)

print("\nTop 10 Most Common Nouns:")
for word, freq in noun_freq.most_common(10):
    print(f"{word}: {freq}")

# --- Generate and display a word cloud ---
print("\nGenerating word cloud...")
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate_from_frequencies(noun_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Nouns in Jane Austen's 'Emma'")
plt.show()

# -------------------------------------------------------------------
# ✅ End of Script
# -------------------------------------------------------------------
print("\nAll NLP tasks completed successfully.")
