# Spell Corrector

Spell corrector that leverages words' context using n-grams and a trained word corpus.
This project combines basic spelling correction techniques with contextual understanding, allowing it to suggest more accurate corrections based on the surrounding words in a sentence.

## Features

- Word Corpus Training: Trains a dictionary of words from a given text file (big.txt) for spelling correction.

- n-gram Training: Utilizes n-grams (default: bigrams) to analyze word sequences and provide context-aware suggestions.

- Edit Distance Corrections: Implements edit distance techniques (one-edit and two-edit corrections) to generate potential word candidates.

- Context-Aware Scoring: Uses n-gram probabilities to resolve ambiguities when multiple correction candidates are available.

- Case Sensitivity: Preserves the capitalization of corrected words to maintain the original style of the input sentence.

## Key Functions

- words(text): Extracts lowercase words from the input text.

- ngrams(words, n=2): Generates n-grams (default: bigrams) from a list of words.

- train_corpus(file_path): Builds a word frequency dictionary from a text corpus.

- train_ngrams(file_path, n=2): Builds an n-gram frequency dictionary from a text corpus.

- edits1(word) and edits2(word): Generate possible corrections within one or two edit distances.

- candidates(word, word_dict): Generates potential correction candidates for a misspelled word.

- context_correction(word_list, word_dict, ngram_dict, n=2): Corrects a list of words using both spelling corrections and n-gram-based context analysis.
