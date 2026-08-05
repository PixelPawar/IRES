from config import APPLICATIONS


def extract_application(query: str):

    query = query.lower()

    for app in APPLICATIONS.values():

        for alias in app["aliases"]:

            if alias in query:
                return app["display"]

    return None