list1 = [1, 2, 3, 4, 5]

list2 = ["A", "B" , "C"]

List3 = ["Hello", 1, True , 245]

print(*list1, sep = " ")

list1.pop(0)

print(*list1, sep = " ")

for x in list1:
    print(x)