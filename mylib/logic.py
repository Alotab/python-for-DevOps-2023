import wikipedia
from textblob import TextBlob


def wiki(name="war Goddess", length=1):
    """This is a wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """search for names from wikipedia"""
    results = wikipedia.search(name)
    return results


def phrase(name):
    """Return phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
