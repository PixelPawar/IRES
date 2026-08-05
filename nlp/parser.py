from nlp.entities import extract_application
from nlp.intents import Intent
from nlp.models import IntentResult
from nlp.patterns import (
    GREETINGS,
    OPEN_WORDS,
    SEARCH_WORDS,
    TIME_WORDS,
)


def parse(query: str) -> IntentResult:

    q = query.lower()

    # Greeting
    if any(word in q for word in GREETINGS):

        return IntentResult(
            intent=Intent.GREETING,
            original_query=query,
        )

    # Time
    if any(word in q for word in TIME_WORDS):

        return IntentResult(
            intent=Intent.ASK_TIME,
            original_query=query,
        )

    # Google Search
    if any(word in q for word in SEARCH_WORDS):

        search_text = q

        for word in SEARCH_WORDS:
            search_text = search_text.replace(word, "")

        return IntentResult(
            intent=Intent.SEARCH_GOOGLE,
            entities={
                "query": search_text.strip()
            },
            original_query=query,
        )

    # Application
    app = extract_application(q)

    if app and any(word in q for word in OPEN_WORDS):

        return IntentResult(
            intent=Intent.OPEN_APPLICATION,
            confidence=0.95,
            entities={
                "application": app
            },
            original_query=query,
        )

    return IntentResult(
        intent=Intent.UNKNOWN,
        confidence=0,
        original_query=query,
    )