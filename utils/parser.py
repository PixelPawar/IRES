import re


OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run"
]


def normalize(text):
    """
    Convert text to lowercase and remove punctuation.
    """

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    return text


def contains_any(text, words):
    """
    Check if any word exists in the text.
    """

    text = normalize(text)

    return any(word in text for word in words)


def is_open_command(query,OPEN_WORDS):
    """
    Determine if the user intends to open something.
    """

    query = normalize(query)

    return contains_any(query, OPEN_WORDS)

from difflib import get_close_matches


def fuzzy_match(text, choices, cutoff=0.6):
    """
    Return the closest matching string from a list of choices.
    Returns None if no good match is found.
    """

    matches = get_close_matches(
        text,
        choices,
        n=1,
        cutoff=cutoff
    )

    return matches[0] if matches else None