from dataclasses import dataclass, field

from nlp.intents import Intent


@dataclass
class IntentResult:
    intent: Intent
    confidence: float = 1.0
    entities: dict = field(default_factory=dict)
    original_query: str = ""