l1=[1,4,5,7,9]
l2=[1,2,3,4,5,6,7,8,9]


for i in range(len(l2)):
    # print(l2[i],end="")
    if l1[i] == l2[i]:
        pass
    else:
        l1.append(l2[i])
        
print(l1,end="")

# for j in range(len(l1)):
#     if l1[j]>l1[j+1]:
#         l1[j],l1[j+1] = l1[j+1],l1[j]
#     print(l1,end="")

# print(list(set(list(l1+l2))))

    
    # Implementing Bubble Sort manually
def bubble_sort(arr):
    n = len(arr)
    print(" ")
    print("n:",n)
    for i in range(n):
        print("#####")
        for j in range(0, n - i - 1):
            print(j,end='')
            if arr[j] > arr[j + 1] :  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr
s1=bubble_sort(l1)  # Sort the list
print()
print("s1:",list(set(s1)))

# print("Updated list:", set(l1))

