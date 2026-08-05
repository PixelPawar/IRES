from speech import say, take_task
from command_processor import process_query
from utils.app_index import build_index


def main():

    say("Assistant activated.")

    while True:
        query = take_task()
        from nlp.parser import parse

        result = parse(query)

        print("\n========== NLP ==========")
        print(result)
        print("=========================\n")
        process_query(query)

if __name__ == "__main__":
    main()