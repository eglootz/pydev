count = 0

for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count = count + 1

# print("We have", count, "even numbers")
print(f"We have {count} even numbers")
