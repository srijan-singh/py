size = int(input("Size of List: "))

num_list = [0 for i in range(size)]

for index in range(size):
    num = int(input("Number: "))
    num_list[index] = num

print(f"The maximum number in list {max(num_list)}")