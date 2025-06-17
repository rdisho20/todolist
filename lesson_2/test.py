def create_greeting():
    greeting = "Hello"

    def display_greeting():
        print(greeting)
    
    # returning function object, not return value of invoked function
    return display_greeting

greet = create_greeting() # 'greet' assigned -> 'display_greeting' func obj
greet() # really calling display_greeting