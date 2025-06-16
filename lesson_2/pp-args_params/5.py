def find_person(**kwargs):
    if "Antonina" in kwargs.keys():
        print(kwargs["Antonina"])
    else:
        print("Antonina not found")

find_person(John="Engineer", Antonina="Software Engineer")
# Antonina's profession is Software Engineer

find_person(John="Engineer", Ginni="Software Engineer")
# Antonina not found