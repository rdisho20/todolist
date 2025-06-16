def calculate_average(*numbers):
    return sum(numbers) / len(numbers) if numbers else None

print(calculate_average())
print(calculate_average(2, 4, 3, 7, 8, 9, 5))