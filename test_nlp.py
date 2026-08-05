from nlp.parser import parse
from nlp.router import route

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    result = parse(query)

    print(result)

    route(result)