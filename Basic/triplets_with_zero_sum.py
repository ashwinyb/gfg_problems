def findTriplets(arr, n):
  #code here
  arr.sort()
  
  for i in range(0, n-1):
    left = i+1
    right = n-1
    curr = arr[i]
    
    while (left<right):
      summ = curr + arr[left] + arr[right]
      
      if summ==0:
        # left+=1
        # right+=1
        return 1
      elif summ<0:
        left += 1
      else:
        right -= 1
  return 0

print(findTriplets([63, -30, 4, 13, 85, -6, 11], 7))