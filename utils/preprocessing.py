import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Tokenization
    words = text.split()

    # Remove stop words
    words = [word for word in words if word not in ENGLISH_STOP_WORDS]

    # Join back into text
    return " ".join(words)