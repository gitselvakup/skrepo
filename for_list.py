from operator import indexOf, index

list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list

for item in new_list:
    print(item)
print("\n")

# second method

list1 = [10, 20, 30, 40, 50]
# get list size
# len(list1) -1: because index start with 0
# iterate list in reverse order
# star from last item to first
size = len(list1) - 1
print(size)
print("This is the output of the second method")
print("\n")
for i in range(size, -1, -1):
     print(list1[i])




