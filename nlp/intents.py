from enum import Enum


class Intent(Enum):
    GREETING = "greeting"

    OPEN_APPLICATION = "open_application"
    OPEN_FILE = "open_file"
    OPEN_FOLDER = "open_folder"
    OPEN_WEBSITE = "open_website"

    SEARCH_GOOGLE = "search_google"

    ASK_TIME = "ask_time"

    AI_QUERY = "ai_query"

    UNKNOWN = "unknown"