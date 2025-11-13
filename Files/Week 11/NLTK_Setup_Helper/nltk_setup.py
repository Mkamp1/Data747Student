"""
NLTK Setup Helper (Enhanced Version)
Author: Michael Kamp
Purpose: Automatically download all required NLTK resources
for use in Data 747 NLP assignments and future projects.
"""

import nltk
import time

print("=" * 60)
print("📘 Starting NLTK setup...")
print("This will download or verify all required resources.")
print("=" * 60)
time.sleep(1)

resources = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "omw-1.4",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "maxent_ne_chunker",
    "maxent_ne_chunker_tab",
    "words",
    "treebank",
    "gutenberg"
]

total = len(resources)
for i, r in enumerate(resources, start=1):
    print(f"\n[{i}/{total}] Downloading: {r} ...")
    try:
        nltk.download(r)
        print(f"✅ {r} complete.")
    except Exception as e:
        print(f"⚠️  Could not download {r}: {e}")
    time.sleep(0.5)

print("\n" + "=" * 60)
print("✅ All available NLTK resources have been downloaded or verified.")
print("You can now safely run your Week 11 scripts:")
print("   python week11_nltk_basic.py")
print("   python week11_nltk_advanced.py")
print("=" * 60)


