
numbers = []

for i in range(3):
    number = int(input(f"Enter integer number {i+1}: "))
    numbers.append(number)


total_sum = sum(numbers)
product = 1
for number in numbers:
    product *= number

average = total_sum / len(numbers)


print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
