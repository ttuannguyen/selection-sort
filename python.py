input = [3, -1, 5, 2]

def selection_sort(input):
    size = len(input)
    for i in range(size):
        inx_of_min = i
        temp = input[i]
        for j in range(i+1, size):
            # print(i, j)
            # update inx of min if current is less than what we had previously
            if input[j] < input[inx_of_min]:
                inx_of_min = j
        input[i] = input[inx_of_min] # move the old min value to the back 
        input[inx_of_min] = temp # move the new min value to the front

print("before:", input)
selection_sort(input)
print("after:", input)
