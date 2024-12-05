numbers = [3,2,1,4,5]
numbers.append(20)
print(numbers)   #[3, 2, 1, 4, 5, 20]

numbers.insert(0,9)   #9 in 0 index
print(numbers)  #[9, 3, 2, 1, 4, 5, 20]       

numbers.remove(4)
print(numbers)   #[9, 3, 2, 1, 5, 20]

numbers.clear()
print(numbers)    #[]

numbers = [1,2,6,4,5]
numbers.pop()
print(numbers)      #[1, 2, 6, 4]

print(numbers.index(2))    #1

print(10 in numbers)      #False


numbers = [1,2,1,4,1]
print(numbers.count(1))    #3


numbers = [1,2,6,4,5]
numbers.sort()
numbers.reverse()
print(numbers)       #[6, 5, 4, 2, 1]


#remove the duplicate
numbers = [1,4,2,6,4,5,2,1]
uniques = []
for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)       #[1, 4, 2, 6, 5]
