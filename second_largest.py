numbers = [10, 40, 20, 50, 30]

largest = max(numbers)
second_largest = None

for number in numbers:
    if number < largest:
        if second_largest is None or number > second_largest:
            second_largest = number

print("Numbers:", numbers)
print("Largest number:", largest)
print("Second largest number:", second_largest)
