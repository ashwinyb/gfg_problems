T = int(input())

for _ in range(T):
    N, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
     
    for _ in range(D):
        A.append(A.pop(0))
    print(*A, end=" ")
    print()