
students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for i in students:
	itemnum = 
	print (itemnum, i['first_name'], i['last_name'], '-', (len(i['first_name']) + len(i['last_name'])))


my_num = [6, 5, 3, 1, 8, 7, 2, 87]
def bubbleSwap(arr):
    for n in range(len(my_num)-1, 0, -1):
        for i in range(n):
            if my_num[i]>my_num[i+1]:
                temp = my_num[i]
                my_num[i] = my_num[i+1]
                my_num[i+1] = temp
bubbleSwap(my_num)
print(my_num)