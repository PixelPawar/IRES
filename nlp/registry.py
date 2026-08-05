from nlp.entities import (
    extract_application,
    extract_folder,
    extract_website,
    extract_file,
)

ENTITY_REGISTRY = {
    "application": extract_application,
    "folder": extract_folder,
    "website": extract_website,
    "file": extract_file,
}