from dataclasses import dataclass, field


@dataclass
class IntentResult:
    """
    Result returned by the NLP parser.
    """

    intent: str
    confidence: float = 1.0
    entities: dict = field(default_factory=dict)
    original_query: str = ""