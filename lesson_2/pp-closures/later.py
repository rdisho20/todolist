def later(func, arguement):

    def new_func():
        return func(arguement)
    
    return new_func

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()


