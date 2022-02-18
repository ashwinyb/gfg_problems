def searchInSorted(arr, N, K):
    #Your code here
    i = 0
    flag = 0
    while i < N and arr[i] <= K:
        if arr[i] == K:
            flag = 1
        i+=1
    if flag == 1:
        return 1
    return -1

# print(searchInSorted([1,3,4,8,10,12], 6, 10))