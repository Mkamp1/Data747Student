import nltk
from nltk import Tree

# Download required data
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample sentence
sentence = "At eight o'clock on Thursday morning... Arthur didn't feel very good."

# Tokenize
tokens = nltk.word_tokenize(sentence)
print("Tokens:", tokens)

# POS Tagging
tagged = nltk.pos_tag(tokens)
print("\nPOS Tags:", tagged[:6])

# Named Entity Recognition
entities = nltk.ne_chunk(tagged)
print("\nNamed Entities:")
print(entities)

# Parse tree example visualization
t = Tree.fromstring('(S (NP (DT The) (NN cat)) (VP (VBD sat) (PP (IN on) (NP (DT a) (NN mat)))))')
t.draw()

# ------------------------------------------------------------
# OUTPUT EXPLANATION
# ------------------------------------------------------------
# This basic demo illustrates the core steps in Natural Language Processing (NLP)
# using NLTK:
#
# 1. Tokenization – breaks a sentence into words.
# 2. POS Tagging – assigns each word a part of speech (NN, VB, JJ, etc.).
# 3. Named Entity Recognition (NER) – identifies entities such as people, places,
#    or organizations (e.g., Arthur → PERSON).
# 4. Parse Tree Visualization – displays a sample syntactic structure for a simple
#    sentence ("The cat sat on a mat") in a pop-up window.
#
# Key takeaway:
# The process transforms raw text into structured data that can be used for
# further analysis such as sentiment, classification, or summarization.
# ------------------------------------------------------------
