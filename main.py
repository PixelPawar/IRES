from speech import say, take_task
from command_processor import process_query
from nlp.parser import parse
from nlp.router import route


def main():
    say("Assistant activated.")

    while True:

        query = take_task()

        if not query:
            continue

        # -----------------------------
        # Parse the user's query
        # -----------------------------
        result = parse(query)

        print("\n========== NLP ==========")
        print(result)
        print("=========================\n")

        # -----------------------------
        # Try the new NLP pipeline
        # -----------------------------
        handled = route(result)

        # -----------------------------
        # Fall back to the old command processor
        # if the router doesn't handle it yet
        # -----------------------------
        if not handled:
            process_query(query)


if __name__ == "__main__":
    main()