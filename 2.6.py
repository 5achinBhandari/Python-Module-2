import random
combination_3_digit = [random.randint(0, 9) for _ in range(3)]
combination_4_digit = [random.randint(1, 6) for _ in range(4)]


print("Random 3-digit combination:")
print(" ".join(map(str, combination_3_digit)))

print("\nRandom 4-digit combination:")
print(" ".join(map(str, combination_4_digit)))
