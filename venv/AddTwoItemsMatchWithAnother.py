
number_array = list()
number = input("Enter the number of elements you want:")
m = int(number)
print ('Enter numbers in array: ')
for i in range(m):
    n = input()
    number_array.append(int(n))
print ('Original Array: ', number_array)
search_number = input("Enter a number which need to match:")
k= int(search_number )
checker = False

for i in range(0,m):
   for j in range(i,m):
       sum = 0;
       sum = number_array[i] + number_array[j]
       if sum == k:
           checker = True
           break
       else:
         continue
   break
print (checker)
