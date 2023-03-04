def linear_search(num_list : list, target : int) -> int :

    for i in range(len(num_list)) :
        if(num_list[i] == target):
            return i

    return -1

def binary_search(num_list : list, target : int, low : int, high : int) -> int :

    if (low < high):

        mid = (low+high)//2

        if(num_list[mid] == target):
            return mid

        elif (num_list[mid] > target):
            return binary_search(num_list, target, low, mid - 1)

        else:
            return binary_search(num_list, target, mid+1, high)

    return -1


num_list = [9, 3, 4, 0, 5, 2, 11]
target = 2

res = linear_search(num_list, target)
print("Linear Search")
print(f"Element found at {res} index" if res != -1 else f"Element is not present!")

low = 0
high = len(num_list)

res = binary_search(num_list, target, low, high)
print("Binary Search")
print(f"Element found at {res} index" if res != -1 else f"Element is not present!")