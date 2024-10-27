# Python program to perform the Binary Search  
  
# Defining a function to perform Binary Search  
# def binarySearch(listt, e, l, h):  
  
#     # We will use two pointers iteration to find the element  
#     while l <= h:  
  
#         mid_element = l + (h - l)//2  
  
#         if listt[mid_element] == e:  
#             return mid_element  
  
#         elif listt[mid_element] < e:  
#             l = mid_element + 1  
  
#         else:  
#             h = mid_element - 1  
  
#     return -1  
  
# # Drivers code  
# listt = [4, 2, 7, 6, 7, 8, 1, 9, 0, 5]  
# e = 7  
  
# index = binarySearch(listt, e, 0, len(listt)-1)  
  
# if index != -1:  
#     print("The element we searched for is present at: " + str(index))  
# else:  
#     print("Not found")  