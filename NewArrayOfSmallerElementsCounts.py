
number_array = list()
new_array = list()
number = input("Enter the number of elements you want:")
m = int(number)
print ('Enter numbers in array: ')
for i in range(m):
    n = input()
    number_array.append(int(n))
print ('Original Array: ', number_array)
for i in range(0,m):
    count = 0;
    for j in range(i+1,m):
        if (number_array[i] > number_array[j]):
            count = count + 1
    new_array.append(count)
print ('New Array: ', new_array)



