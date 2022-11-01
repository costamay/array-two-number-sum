# def sol(A, T):
    
#     new_list = []
#     for i in A:
#         num = str(i)
#         total = int(num[0]) + int(num[1])
        
#         if total == T:
#             new_list.append(i)
#     return new_list

# print(sol([3,5,-4,8,11,1,-1,6], 10))

def twoNumberSum(array, targetSum)::
    seen = {}
    new_list = []
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                new_list.append(array[i])
                new_list.append(array[j])

    return new_list

print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))