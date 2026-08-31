import nltk

_REQUIRED_NLTK_DATA = {
    "stopwords": "corpora/stopwords",
    "rslp": "stemmers/rslp",
}


def ensure_nltk_data() -> None:
    for package, path in _REQUIRED_NLTK_DATA.items():
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(package)
