
number_array = list()
product_number_array = list()
number = input("Enter the number of elements you want:")
m = int(number)
print ('Enter numbers in array: ')
for i in range(m):
    n = input()
    number_array.append(int(n))
print ('Original Array: ', number_array)
for i in range(m):
     prod =1
     for j in range(m):
         if i != j:
             prod = prod * number_array[j]
     product_number_array.append(prod)
print ('Product Array: ', product_number_array)