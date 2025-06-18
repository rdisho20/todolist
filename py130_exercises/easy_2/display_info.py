def display_info(data, /, *, reverse=False, uppercase=False):
    if not reverse and not uppercase:
        return data
    if reverse and uppercase:
        return data.upper()[::-1]
    if not reverse:
        return data.upper()
    if not uppercase:
        return data[::-1]

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC