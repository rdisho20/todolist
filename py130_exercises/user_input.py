def input_generator():
    user_input = None

    while user_input != "stop":
        user_input = input("type input: ")
        yield user_input

for entry in input_generator():
    print(entry)