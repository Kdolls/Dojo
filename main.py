""""lists"""""

# # maximum element in a list
# # Explanation: The max() function returns the maximum element from the given list.
#
# #
# # def find_max_element(l):
# #     return max(l)
# # # Test
# # print(find_max_element([10, 5, 7, 15, 3]))
#
# #
# # Write a Python program to reverse a given list.
# # Explanation: The slicing syntax [::-1] reverses the list.
#
# # def rev(x):
# #     return x[::-1]
# #
# # print(rev([1,2,3,4,5,6,7,8]))
#
# # Write a Python program to sort a list of numbers in ascending order.
# # Explanation: The sorted() function returns a new sorted list.
#
# # def sort(x):
# #     return sorted(x)
# #
# # print(sort([1,2,3,44,4,5,8,6,6]))
#
# # Write a Python program to remove a specific element from a list.
# # Explanation: The remove() method removes the first occurrence of the specified element from the list.
#
# # How to append an element to a list?
# # my_list = [1, 2, 3, 4]
# # my_list.append(99)
# # print(my_list)
# # Explanation: The append() method adds the specified element to the end of the list.
#
#
# # How to remove an element from a list?
# # my_list = [1, 2, 3, 4, 5, 6, 7]
# # my_list.remove(4)
# # print(my_list)
#
# # Explanation: The remove() method removes the first occurrence of the specified element from the list.
#
# # How to insert an element at a specific position in a list?
# # my_list = [1, 2, 3, 5, 6, 7]
# # my_list.insert(3,4)
# # print(my_list)
#
#
# # Explanation: The insert() method inserts the specified element at the specified position in the list.
# # my_list = [1, 2, 3, 4, 5, 6, 7]
# # my_list.remove(4)
# # print(my_list)
#
#
# # How to extend a list with another list?
# # my_list = [1, 2, 3, 4, 5, 6, 7]
# # my_list_2= [1, 2, 3, 4, 5, 6, 7]
# # my_list.extend(my_list_2)
# # print(my_list)
#
#
# # Explanation: The extend() method adds all the elements of the specified list to the end of the current list.
#
# # How to reverse the elements of a list?
# # my_list = [1, 2, 3, 4, 5, 6, 7]
# # my_list.reverse()
# # print(my_list)
#
#
# # Explanation: The reverse() method reverses the elements of the list in place.
#
# # How to sort elements in a list in ascending order?
# # my_list = [1, 2, 3, 4, 5, 6, 7]
# # my_list_2 = [9,8,7,6,5,4,3]
# # my_list_2.sort()
# # print(my_list_2)
# # # Explanation: The sort() method sorts the elements of the list in ascending order.
#
# # How to get the index of a specific element in a list?
# #
# # my_list = [1, 2, 3, 4, 5, 6, 7]
# # my_list_2 = [9,8,7,6,5,4,3]
# # print('the index number is : ',my_list_2[3])
#
# # Explanation: The index() method returns the index of the first occurrence of the specified element in the list.
#
#
# How to create a list with integers from 1 to 10?
# Explanation: Use list comprehension to generate a list of integers from 1 to 10.
# mylist = [x for x in range(1,111)]
# print(mylist)

# python
#
#
# How to access the last element of a list?
# Explanation: Use negative indexing to access the last element of a list.
# my_list_2 = [9,8,7,6,5,4,3]
# print(my_list_2[-1])

#
# python
#
#
#
# How to check if an element exists in a list?
#
# Explanation: Use the in operator to check if an element exists in a list.
# my_list_2 = [9,8,7,6,5,4,3]
# if 4 in my_list_2:
#     print('its here')
# # python
#
#
#
# How to slice a list to get the first three elements?
#
# Explanation: Use slicing to get a sublist of the first three elements.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# print(my_list_2[:3])

# python
#
#
#
# How to count the number of elements in a list?
#
# Explanation: Use the len() function to get the length of the list.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# print(len(my_list_2))

# python
#
#
#
# How to find the sum of elements in a list?
#
# Explanation: Use the sum() function to find the sum of elements in a list.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# print(len(my_list_2))
# python
#
#
#
# How to remove the first element from a list?
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# print(my_list_2[1:])
# Explanation: Use slicing to remove the first element from a list.
#
# python
#
#
# How to reverse a list in place?
#
# Explanation: Use the reverse() method to reverse a list in place.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_2.reverse()
#
# print(my_list_2)
# python
#
#
#
# How to sort a list in ascending order?
#
# Explanation: Use the sort() method to sort a list in ascending order.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_2.sort()
#
# print(my_list_2)
# # python
#
#
#
# How to find the index of a specific element in a list?
#
# Explanation: Use the index() method to find the index of a specific element.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_2.index(23)
#
# print(my_list_2.index(23))
# # python
# #
# #
# # How to add elements from one list to another list?
# #
# # Explanation: Use the extend() method to add elements from one list to another list.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_3 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
#
# my_list_2.extend(my_list_3)
#
# print(my_list_2)
# python
#
#
#
# How to remove all occurrences of an element from a list?
#
# Explanation: Use list comprehension to filter out the elements to remove.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_3 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
#
# print([e for e in my_list_3 if e != 23])
# python
#
#
#
# How to find the maximum and minimum elements in a list?
#
# Explanation: Use the max() and min() functions to find the maximum and minimum elements in a list, respectively.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_3 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
#
# print(max(my_list_3), min(my_list_2))

# python
#
#
#
# How to check if all elements in a list are the same?
#
# Explanation: Use the all() function to check if all elements in a list are the same.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_3 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
#
# print(all(x == my_list_2[0] for x in my_list_2))
# python
#
#
#
# How to count the occurrences of each element in a list?
#
# Explanation: Use a dictionary to count the occurrences of each element.
# my_list_2 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
# my_list_3 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7]
#
# print(my_list_2.count(332))
# # python
#
#
#
# How to remove duplicates from a list?
#
# Explanation: Convert the list to a set to remove duplicates and then convert it back to a list.
# my_list_3 = [12, 23, 332, 3, 6, 7, 8, 9, 5, 6, 7,7,97]
# mod = (set(my_list_3))
# print(mod)
# python
#
#
#
# How to create a list of lists in Python?
#
# Explanation: Lists can contain elements of any type, including other lists.
#
# python
#
# How to check if two lists are equal in Python?
#
# Explanation: Use the == operator to check if two lists are equal.
#
# python
#
#
#
# How to iterate over a list and its indices simultaneously?
#
# Explanation: Use the enumerate() function to get both the index and the element in each iteration.
#
# python
#
#
#
# How to find the average of elements in a list?
#
# Explanation: Calculate the sum of elements and divide by the length of the list.
#
# python
#
#
#
# How to insert an element at a specific index in a list?
#
# Explanation: Use the insert() method to insert an element at a specific index.
#
# python
#
#
# How to check if a list is empty or not?
#
# Explanation: Use the truthiness of the list to check if it's empty.
#
# python
#
#
#
# How to remove elements from a list by value?
#
# Explanation: Use list comprehension to filter out elements to be removed.
#
# python
#
#
#
# How to concatenate multiple lists in Python?
#
# Explanation: Use the + operator to concatenate multiple lists.
#
# python
#
#
#
# How to remove elements from a list by index?
#
# Explanation: Use slicing to remove elements by index.
#
# python
#
#
#
# How to check if two lists have at least one common element?
#
# Explanation: Use set intersection to check if two lists have at least one common element.
#
# python
#
#
# How to sort a list of strings alphabetically?
#
# Explanation: Use the sorted() function to sort a list of strings alphabetically.
#
# python
#
#
#
# How to find the most common element in a list?
#
# Explanation: Use the Counter class from the collections module to find the most common element.
#
# python
#
#
#
# How to check if all elements in a list are integers?
#
# Explanation: Use list comprehension and the isinstance() function to check if all elements are integers.
#
# python
#
#
# How to remove elements from a list that are duplicates from another list?
#
# Explanation: Use list comprehension to filter out elements from the first list that are not duplicates in the second list.
#
"""Dictionary"""

#
# 1. How to Add an Element to a Dictionary?
# my_diction = {'x': 1, 'y': 3, 'mickey': 'mouse', 76: 'street'}
# # Define a dictionary
# # Add a new key-value pair
# print(my_diction)
#
# # Explanation: To add an element to a dictionary, you can simply assign a value to a new key.
# # 2. How to Update the Value of an Existing Key in a Dictionary?
# my_diction = {'x': 1, 'y': 3, 'mickey': 'mouse', 76: 'street'}
# my_diction['mini'] = 48
# my_diction['x'] = 23
# print(my_diction)

# python
#
# # Define a dictionary
#
# # Update the value of key 'b'
#
#
# Explanation: To update the value of an existing key in a dictionary, you can simply assign a new value to that key.
# 3. How to Remove an Element from a Dictionary?
#
# python
#
# # Define a dictionary
# my_diction = {'x': 23, 'y': 3, 'mickey': 'mouse', 76: 'street', 'mini': 48}
#
# del my_diction['mini']
# print(my_diction)
# #
#
# Explanation: To remove an element from a dictionary, you can use the del keyword followed by the key you want to remove.
# 4. How to Iterate Through a Dictionary?
#
# python
#
# # # Define a dictionary
# my_diction = {'x': 23, 'y': 3, 'mickey': 'mouse', 76: 'street', 'mini': 48}
#
# # # Iterate through the dictionary
# for x, y in my_diction.items():
#     print(x, y)


# Explanation: You can use the .items() method to iterate through the key-value pairs of a dictionary.
# 5. How to Check if a Key Exists in a Dictionary?
#
# python
#
# # Define a dictionary
my_diction = {'x': 23, 'y': 3, 'mickey': 'mouse', 76: 'street', 'mini': 48}
if 'mouse' in my_diction:
        del my_diction['mouse']
print(my_diction)
# # Check if 'b' is a key in the dictionary
