size = int(input("Size of List: "))

name_list = [' ' for i in range(size)]

for index in range(size):
    name = input("Name: ")
    name_list[index] = name

print(f"List before sorting {name_list}")
name_list.sort()
print(f"List after sorting {name_list}")