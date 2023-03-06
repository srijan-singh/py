def factorial_rec(num):
    if num == 1:
        return 1

    return num * factorial(num-1)

def factorial_iter(num):
    res = 1

    for num in range(1, num+1):
        res*=num

    return res

num = int(input("Number:"))

print(f"Factorial of {num} is {factorial(num)}")