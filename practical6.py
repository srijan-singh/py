def fib(num):
    
    if num == 1 or num == 0:
        return num

    return fib(num-1) + fib(num-2)

num = int(input("Number: "))

print(f"Fibbonaci series of {num} is {fib(num)}")
    