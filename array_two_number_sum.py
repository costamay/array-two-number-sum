def sol(A, T):
    
    new_list = []
    for i in A:
        num = str(i)
        total = int(num[0]) + int(num[1])
        
        if total == T:
            new_list.append(i)
    return new_list

print(sol([64, 23,24, 25, 55], 10))
