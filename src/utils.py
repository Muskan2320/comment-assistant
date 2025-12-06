import re
import nltk
from nltk.data import find
from nltk.stem import WordNetLemmatizer

def safe_nltk_download(resource_path, download_name):
    try:
        find(resource_path)
    except LookupError:
        nltk.download(download_name)

safe_nltk_download("tokenizers/punkt", "punkt")
safe_nltk_download("tokenizers/punkt_tab", "punkt_tab")
safe_nltk_download("corpora/wordnet", "wordnet")
safe_nltk_download("corpora/omw-1.4", "omw-1.4")

lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    """
    Basic cleaning: lowercasing, remove URLs, mentions, non-letters.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " url ", text)
    text = re.sub(r"@\w+", " user ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def lemmatize_text(text: str) -> str:
    tokens = nltk.word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(tok) for tok in tokens]
    return " ".join(lemmas)

def preprocess(text: str) -> str:
    return lemmatize_text(clean_text(text))
