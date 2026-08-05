from nlp.intents import Intent
from nlp.models import IntentResult
from nlp.entities import extract_application


def parse(query: str):

    q = query.lower()

    if any(word in q for word in ["hello", "hi", "hey"]):

        return IntentResult(
            intent=Intent.GREETING,
            original_query=query
        )

    app = extract_application(q)

    if app:

        return IntentResult(
            intent=Intent.OPEN_APPLICATION,
            entities={
                "application": app
            },
            confidence=0.95,
            original_query=query
        )

    return IntentResult(
        intent=Intent.UNKNOWN,
        confidence=0.0,
        original_query=query
    )