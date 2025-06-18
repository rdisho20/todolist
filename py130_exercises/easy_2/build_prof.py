def build_profile(first, last, **kwargs):
    profile = {
        "first_name": first,
        "last_name": last
    }

    for key, value in kwargs.items():
        profile[key] = value
    
    return profile

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}