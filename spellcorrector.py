import re
from collections import Counter, defaultdict

def words(text):
    """Extract words from text, converting to lowercase."""
    return re.findall(r'\w+', text.lower())

def ngrams(words, n=2):
    """Generate n-grams from a list of words."""
    """I like to code"""
    """zip(['I', 'like', 'to', 'code'], ['like', 'to', 'code'])"""
    """[('I', 'like'), ('like', 'to'), ('to', 'code')]"""
    return zip(*[words[i:] for i in range(n)])

def train_ngrams(file_path, n=2):
    """Train n-grams from a text corpus."""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = words(text)
    return Counter(ngrams(tokens, n))


def train_corpus(file_path):
    """Train a dictionary from a text corpus."""
    """This is a test. This is only a test."""
    """Counter({'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1})"""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return Counter(words(text))

def edits1(word):
    """Return all edits that are one edit away from the input word."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def known(words, word_dict):
    """Filter words that are present in the dictionary."""
    return set(w for w in words if w in word_dict)

def edits2(word):
    """Return all edits that are two edits away from the input word."""
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def candidates(word, word_dict):
    """Generate possible spelling corrections for the word."""
    return (known([word], word_dict) or
            known(edits1(word), word_dict) or
            known(edits2(word), word_dict) or
            {word})

def context_correction(word_list, word_dict, ngram_dict, n=2):
    """Correct words using context from surrounding words."""
    corrected_words = []
    for i, word in enumerate(word_list):
        if word.lower() in word_dict:
            corrected_words.append(word)
            continue

        context_candidates = candidates(word.lower(), word_dict)
        if len(context_candidates) > 1:
            # Use n-gram probabilities for tie-breaking
            prev_word = corrected_words[-1].lower() if i > 0 else None
            next_word = word_list[i + 1].lower() if i + 1 < len(word_list) else None

            context_scores = defaultdict(int)
            for candidate in context_candidates:
                if prev_word:
                    context_scores[candidate] += ngram_dict.get((prev_word, candidate), 0)
                if next_word:
                    context_scores[candidate] += ngram_dict.get((candidate, next_word), 0)
            best_candidate = max(context_scores, key=context_scores.get, default=word.lower())
        else:
            best_candidate = next(iter(context_candidates))

        # Preserve capitalization
        if word[0].isupper():
            best_candidate = best_candidate.capitalize()

        corrected_words.append(best_candidate)
        print(f"Corrected '{word}' to '{best_candidate}' using context.")
    return corrected_words

word_dict = train_corpus('C:\pjn\\big.txt')
ngram_dict = train_ngrams('C:\pjn\\big.txt', n=2)

sentence = "They ae goin to thear hose"
corrected_sentence = context_correction(sentence.split(), word_dict, ngram_dict)
print(' '.join(corrected_sentence))

print("\n\n")
sentence = "I goe to scholl evry day"
corrected_sentence = context_correction(sentence.split(), word_dict, ngram_dict)
print(' '.join(corrected_sentence))

print("\n\n")
sentence = "I liek to eat aplle pie"
corrected_sentence = context_correction(sentence.split(), word_dict, ngram_dict)
print(' '.join(corrected_sentence))





