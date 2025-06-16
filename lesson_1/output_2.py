file = open('output.txt', 'a')
file.write("Third line\n")
file.write("Last line\n")

lines = ["Just kidding!\n", "Hahaha!\n"]
file.writelines(lines)
file.close()