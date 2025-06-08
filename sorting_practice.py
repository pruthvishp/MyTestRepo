import os
def bubble_sort(num_list: list)-> list:
    n = len(num_list)
    for i in range(0,n):
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
           # print(num_list)
    return num_list

def insertion_sort(num_list: list)-> list:
    n = len(num_list) 
    for i in range(1,n):
        val = num_list[i]
        j = i-1
        while(j>=0 and num_list[j]>val):
            num_list[j+1]= num_list[j]
            j = j-1
        num_list[j+1] = val
    return num_list

def selection_sort(num_list: list)-> list:
    l = len(num_list)
    for i in range(l):
        #k = num_list[i]
        for j in range(i,l):
            if num_list[i] > num_list[j]:
                num_list[i],num_list[j] = num_list[j],num_list[i]
    return num_list

def bubble_sort2(num_list: list)-> list:
    n = len(num_list)
    for i in range(n-1):
        for j in range(n-1-i):
            if num_list[j]>num_list[j+1]:
                num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
    return num_list

def insertion_sort2(num_list:list) -> list:
    n = len(num_list)
    for i in range(1,n):
        k = num_list[i]
        j = i-1
        while(j>=0 and num_list[j]>k):
            num_list[j+1] = num_list[j] #right shift
            j = j-1
        num_list[j+1] = k
    return num_list

def quick_sort(num_list: list)->list:
    if len(num_list) <= 1:
        return num_list
    n = len(num_list)
    pivot_index = 0
    pivot_val = num_list[pivot_index]
    left_part = []
    equal_part = []
    right_part= []
    for index in range(n):
        if num_list[index]<pivot_val:
            left_part.append(num_list[index])
        elif num_list[index]>pivot_val:
            right_part.append(num_list[index])
        else:
            equal_part.append(num_list[index])
    return quick_sort(left_part) + equal_part + quick_sort(right_part)

        
          




    
        


print(bubble_sort([2,4,2,4,2,5,3,5,3,8]))
print(bubble_sort2([2,4,2,4,2,5,3,5,3,8]))
print(insertion_sort([2,4,2,4,2,5,3,5,3,8]))
print(insertion_sort2([2,4,2,4,2,5,3,5,3,8]))
print(selection_sort([2,4,2,4,2,5,3,5,3,8]))

print(quick_sort([2,4,2,4,2,5,3,5,3,8]))


