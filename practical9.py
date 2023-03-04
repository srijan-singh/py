def sumList(num_list : list) -> int:
    total_sum = 0

    for num in num_list:
        total_sum+=num

    return total_sum

size = int(input("Size of List: "))

num_list = [0 for i in range(size)]

for index in range(size):
    num = int(input("Number: "))
    num_list[index] = num

print(f"Sum of list {num_list} is {sumList(num_list)}")


