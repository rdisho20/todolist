def register(username, /, age=0, *, password=''):
    print(f"{username}'s age is {age}.  Password = {password}")

register("YoYo", password="123456789")
register("YoYo2", age=40, password="123456789")
register("YoYo3", 25, password="123456789")