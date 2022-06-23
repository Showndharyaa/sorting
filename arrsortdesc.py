#Program to check if the array is descending order

arr=[10,19,16,30,65]
sorted_arr = arr.sort()

if (arr == sorted_arr):
  print ("arr is in non-decreasing order")
else:
  print ("arr is not in non-decreasing order")
