for i in range(1, 11):
    print('Current value:', i)


print("\n")

# second for_loop program
print("second for_loopwith list statement")
print("##################################")
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for x in list1:
    for y in list2:
        print(x,y)

print("\n")

# third for_loop program
# break statement
print("third for_loopwith break/continue statement")
print("##################################")

vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        break
    print(v)

print("\n")

# fourth  for_loop program
# Multiplication
print("third for_loop with multiplication statement")
print("###########################################")
numbers = [2,5,6,10,15,20,25]

for n in numbers:
    if n%3 == 0:
        print(n)

print("\n")

# five
#ascedning order / descending order
print("five for_loop with ascedning order / descending order")
print("#####################################################")
numbers = [19,4,50,80,12]

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i] > numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j];
            numbers[j] = temp

print(numbers)