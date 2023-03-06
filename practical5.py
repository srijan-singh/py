def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num-1)

num = int(input("Number:"))

print(f"Factorial of {num} is {factorial(num)}")