from enum import Enum


class Intent(Enum):

    OPEN_APPLICATION = "open_application"
    OPEN_FILE = "open_file"
    OPEN_FOLDER = "open_folder"

    SEARCH_GOOGLE = "search_google"

    OPEN_WEBSITE = "open_website"

    ASK_TIME = "ask_time"

    AI_QUERY = "ai_query"

    GREETING = "greeting"

    UNKNOWN = "unknown"