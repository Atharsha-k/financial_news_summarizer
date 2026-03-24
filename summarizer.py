import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


def summarize_text(text, num_sentences=3):
    # Safety check
    if not text or len(text.strip()) == 0:
        return "No input text provided."

    # Tokenize sentences
    sentences = sent_tokenize(text)

    if len(sentences) == 0:
        return "Not enough content to summarize."

    # Preprocess words
    stop_words = set(stopwords.words("english"))
    word_frequencies = {}

    for word in word_tokenize(text.lower()):
        if word not in stop_words and word not in string.punctuation:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    if len(word_frequencies) == 0:
        return "Unable to process text."

    # Score sentences
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Sort sentences by score
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    # Limit number of sentences
    num_sentences = min(num_sentences, len(sorted_sentences))

    summary = " ".join(sorted_sentences[:num_sentences])

    return summary


# 🔹 Test the file independently
if __name__ == "__main__":
    sample_text = """Stock markets surged today as investors reacted positively to new economic data.
    The central bank indicated that interest rates will remain stable.
    Technology stocks led the gains with strong earnings.
    Analysts believe this trend may continue if inflation remains under control."""

    print("Original Text:\n", sample_text)
    print("\nSummary:\n", summarize_text(sample_text, 2))