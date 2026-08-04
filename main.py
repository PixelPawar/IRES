from speech import say, take_task
from command_processor import process_query

def main():
    say("Assistant activated.")

    while True:
        query = take_task()
        process_query(query)

if __name__ == "__main__":
    main()