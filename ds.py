# # Python program to show how to create a binary tree and traverse it in Python  
  
# # Creating a class for a Node of the tree  
# class Node:  
#     def __init__(self, value):  
#         self.left = None  
#         self.val = value  
#         self.right = None  
  
#     # Method to transverse in a pre-order manner  
#     def traverseAsPreOrder(self):  
#         print(self.val, end = ' ')  
#         if self.left != None:  
#             self.left.traverseAsPreOrder()  
#         if self.right != None:  
#             self.right.traverseAsPreOrder()  
  
#     # Method to transverse in an in-order manner  
#     def traverseAsInOrder(self):  
#         if self.left != None:  
#             self.left.traverseAsInOrder()  
#         print(self.val, end = ' ')  
#         if self.right != None:  
#             self.right.traverseAsInOrder()  
  
#     # Method to transverse in an post-order manner  
#     def traverseAsPostOrder(self):  
#         if self.left != None:  
#             self.left.traverseAsPostOrder()  
#         if self.right != None:  
#             self.right.traverseAsPostOrder()  
#         print(self.val, end = ' ')  
  
# # Drivers code for the above binary tree class  
# root_node = Node(4)  
  
# root_node.left = Node(5)  
# root_node.right = Node(7)  
# root_node.right.left = Node(2)  
# root_node.right.left.right = Node(9)  
# root_node.left.right = Node(0)  
# root_node.left.left = Node(10)  
# root_node.left.left.right = Node(1)  
  
# # Transferring the tree  
# print("Pre-order traversal of the tree: ", end = "")  
# root_node.traverseAsPreOrder()  
# print("\nIn-order traversal of the tree: ", end = "")  
# root_node.traverseAsInOrder()  
# print("\nPost-order traversal of the tree: ", end = "")  
# root_node.traverseAsPostOrder()  
# Python program to implement Bubble Sort Algorithm   
  
# Creating a method to perform bubble sort  
# def bubbleSort(listt):  
      
#   # looping over each element of the list  
#   for c in range(len(listt)):  
  
#     # looping over remaining elements to compare with the current element  
#     for n in range(0, len(listt) - c - 1):  
  
#         # comparing the two adjacent elements  
#         # we are sorting in descending order   
#         if listt[n] < listt[n + 1]:  
  
#             # Swapping the two elements if they are not in the correct order  
#             temporary = listt[n]  
#             listt[n] = listt[n + 1]  
#             listt[n + 1] = temporary  
  
# # Drivers code for the above method  
# listt = [3, 7, 9, 2, 5, 0]  
  
# bubbleSort(listt)  
  
# print('Sorted List in Descending Order:')  
# print(listt)  
# Python program to implement Selection Sort   
  
# Defining a method to perform Selection Sort  
# def selectionSort(listt, size):  
     
#     for s in range(size):  
#         max_index = s  
  
#         for i in range(s + 1, size):  
           
#             # We are sorting in descending order  
#             # Selecting the maximum element of the listt  
#             if listt[i] > listt[max_index]:  
#                 max_index = i  
           
#         # putting the maximum value at the beginning of the list  
#         (listt[s], listt[max_index]) = (listt[max_index], listt[s])  
  
# # Drivers code  
# listt = [20, 35, 29, 85, 23, 97]  
# size = len(listt)  
# selectionSort(listt, size)  
# print('Sorted List in Descending Order:')  
# print(listt)  
# Python program to perform Quick Sort Algorithm  
  
# Defining a function to search for the pivoting position  
# def pivot(listt, low, high):  
  
#   # selecting the right-most element as a pivot  
#   pivot = listt[high]  
  
#   # the greater item  
#   g = low - 1  
  
#   # transversing through all the elements  
#   for i in range(low, high):  
#     if listt[i] <= pivot:  
#       # if the value of j is smaller, we will swap it with the pointer g  
#       g = g + 1  
  
#       # swap the elements at g and i  
#       (listt[g], listt[i]) = (listt[i], listt[g])  
  
#   # swapping the pivot with the element of greater value  
#   (listt[g + 1], listt[high]) = (listt[high], listt[g + 1])  
  
#   # returning the position from where the pivot is done  
#   return g + 1  
  
# # defining a function to perform Quick Sort  
# def quickSortAlgo(listt, low, high):  
#     if low < high:  
  
#         # searching the pivot for which elements on its left are smaller and elements on its right are greater  
#         p = pivot(listt, low, high)  
  
#         # calling left pivot recursively  
#         quickSortAlgo(listt, low, p - 1)  
  
#         # calling right pivot recursively  
#         quickSortAlgo(listt, p + 1, high)  
  
# # Drivers code  
# listt = [3, 7, 2, 4, 9, 1, 0, 8]  
  
# size = len(listt)  
  
# quickSortAlgo(listt, 0, size - 1)  
  
# print('Sorted List in Ascending Order:')  
# print(listt)  
