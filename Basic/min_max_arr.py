def getMinMax(a, n):
    
    a = sorted(a)
    return a[0], a[-1]

print(getMinMax([32,44,12,33,221], 5))