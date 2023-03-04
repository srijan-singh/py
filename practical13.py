def bubble_sort(num_list : list) -> list :
    size = len(num_list)

    for i in range(size):
        for j in range(i+1, size):
            if(num_list[i] > num_list[j]):
                num_list[i], num_list[j] = num_list[j], num_list[i]
    
    return num_list


num_list = [3,2,1,4,9,0]
print(num_list)
bubble_sort(num_list)
print(num_list)