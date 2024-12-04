names = ['jontu','montu','sontu','bontu']

print(names[-1])         #bontu
print(names[2:])      #['sontu', 'bontu']
print(names[1:3])     #['montu', 'sontu']

#maximum number
numbers = [3,6,3,2,4,7,1]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)        