num = int(input("Number: "))

PRIME = True

for factor in range(2, num):
    if num % factor == 0:
        PRIME = False
        break

if PRIME:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number, it has a factor other than one and iteslf; which is {factor}")
        
