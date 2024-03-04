#Empty list
my_list = []

#Appending the following elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

#Inserting 15 at the second position in the list
my_list.insert(1, 15)

#Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

#Removing the last element from my_list
my_list.pop()

#Sorting my_list in ascending order
my_list.sort()

#Finding and printing the index of the 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)

#Printing my_list
print("My Final List is:", my_list)