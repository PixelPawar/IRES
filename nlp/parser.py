from nlp.intents import Intent
from nlp.models import IntentResult
from nlp.patterns import (
    GREETINGS,
    OPEN_WORDS,
    SEARCH_WORDS,
    TIME_WORDS,
)
from nlp.registry import ENTITY_REGISTRY


def parse(query: str) -> IntentResult:
    """
    Parse the user's query and return the detected intent,
    confidence score and extracted entities.
    """

    q = query.lower()

    # -----------------------------
    # Greeting
    # -----------------------------
    if any(word in q for word in GREETINGS):
        return IntentResult(
            intent=Intent.GREETING,
            confidence=1.0,
            original_query=query,
        )

    # -----------------------------
    # Time
    # -----------------------------
    if any(word in q for word in TIME_WORDS):
        return IntentResult(
            intent=Intent.ASK_TIME,
            confidence=1.0,
            original_query=query,
        )

    # -----------------------------
    # Google Search
    # -----------------------------
    if any(word in q for word in SEARCH_WORDS):

        search_text = q

        for word in SEARCH_WORDS:
            search_text = search_text.replace(word, "")

        return IntentResult(
            intent=Intent.SEARCH_GOOGLE,
            confidence=1.0,
            entities={
                "query": search_text.strip()
            },
            original_query=query,
        )

    # -----------------------------
    # Entity Detection
    # -----------------------------
    entity_type = None
    entity_value = None

    for name, extractor in ENTITY_REGISTRY.items():

        value = extractor(q)

        if value:
            entity_type = name
            entity_value = value
            break

    # -----------------------------
    # Open commands
    # -----------------------------
    if any(word in q for word in OPEN_WORDS):

        if entity_type == "application":

            return IntentResult(
                intent=Intent.OPEN_APPLICATION,
                confidence=0.95,
                entities={
                    "type": entity_type,
                    "value": entity_value,
                },
                original_query=query,
            )

        elif entity_type == "folder":

            return IntentResult(
                intent=Intent.OPEN_FOLDER,
                confidence=0.95,
                entities={
                    "type": entity_type,
                    "value": entity_value,
                },
                original_query=query,
            )

        elif entity_type == "website":

            return IntentResult(
                intent=Intent.OPEN_WEBSITE,
                confidence=0.95,
                entities={
                    "type": entity_type,
                    "value": entity_value,
                },
                original_query=query,
            )

        elif entity_type == "file":

            return IntentResult(
                intent=Intent.OPEN_FILE,
                confidence=0.95,
                entities={
                    "type": entity_type,
                    "value": entity_value,
                },
                original_query=query,
            )

    # -----------------------------
    # Unknown
    # -----------------------------
    return IntentResult(
        intent=Intent.UNKNOWN,
        confidence=0.0,
        original_query=query,
    )