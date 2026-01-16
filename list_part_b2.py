#Various operations
print("**********************list Methods********************")

#append()
print("*********************append***************************")
numbers=[1,4,5,6,10,"Devi","bhargavi",2.5,6.4,4]
numbers.append("Lahari")
print(numbers)


#Extend
print("**************extend*************************")
numbers.extend(["sai",2.4,96])
print(numbers)

#copy
print("****************copy******************")
number2=numbers.copy()
print(number2)
number2.append("Python life")
print(number2)

#clear
print("*********************clear************************")
number3=number2.copy()
print(number3)
number3.clear()
print(number3)

#count
print("*****************count*********************")
number3.append("cricket")
print(number3)
number3.extend([1,4,6.2,5,8.4,66,"chinnu","adhi",6])
print(number3)
print("count of 6")
print(number3.count(6))


#index
#print("******************Index**********************")
#print(number3.index(5.8))


#Remove
print("*********************Remove***********************")
print(number3)
number3.remove(4)
print(number3)


#pop
print("***************Pop***********************")
print(number3)
number3.pop(6)
print(number3)


#insert
print("*******************Insert*********************")
number3.insert(6,"Mango")
print(number3)
number3.insert(7,"apple")
print(number3)


#Reverse
print("*****************reverse************************")
print(number3)
number3.reverse()
print(number3)


#sort
print("********************sort********************")
number4=[3,4,6,9]
print(number4)
number4.sort()
print(number4)
number4.sort(reverse=True)
print(number4)


#list comprehesions
print("********************list comprehensions*********************")

for x in range(11):
    result1=x**2
    print(result1)

    print([x**2 for x in range(11)])

    print([k for k in [1,2,4,5,6,7]if k%2==0])

    print("**************remove values*******************")
    list_10=[1,5,6,7,8,9,10]
    print(list_10)
    u=int(input("Enter Input value 1 to 10"))
    for y in list_10:
        if y==u:
            list_10.remove(y)
            print(y)

            print(list_10)


#length
print("************length*********************")
print(list_10)
y=list_10__len__()
print(y)


empty_list=[]
empty_list=list_10.copy()
print(empty_list)
empty_list.extend([11,12,13])
print(empty_list)


#Coding Exercise 
print("********************Coding Exercise*****************")


#Reverse List
print("*******************Revrse List***************")

my_list=[10,20,30,40,50]
print('before reverse',my_list)
my_list.reverse()
print('after reverse',my_list)


#Common Elements
print("********************common elements**********************")
input_2=[2,3,4,5,6]
input_3=[4,6,7,9,1]
print(input_2)
print(input_3)
comm_list=[]
for m in input_2:
    for n in input_3:
        if m==n:
            comm_list.append(m)
print(comm_list)


#unique elements
print("***********Unique Element***************")
original_list=[1,2,2,3,4,4,5]
print(original_list)
unique_list=set(original_list)
print("unique list",unique_list)

print("****************Remove Duplicate********************")
O_list=[1,2,23,4,4,5]
u_list2=[]
for p in o_list:
    if p not in u_list2:
        u_list2.append(p)

print(u_list)


#list Concatenation

print("*****************List Concatenation********************")


a_list=[1,2,3,4]
b_list=[5,6,7]
print(a_list)
print(b_list)
result_c_list=a_list+b_list
print(result_c_list)


#List Repetition
print("*****************List Repetition*********************")
for r in range(3):
    print(a_list)


#List Removal
print("***************List Removal*******************")

a_list.remove(2)
print(a_list)

#List Insertion
print("*************List Insertion*********************")


a_list.insert(0,10)
a_list.insert(1,10)
a_list.insert(2,11)
print(a_list)


#list comprehensions
print("*******************List comprehensions*******************")

#square Numbers
print("*****************Square Numbers 1 to 10****************")

print([s**2 for s in range(1,11)])
#Even Numbers
print("****************Even Number*********************")
print([t for t in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]if t%2==0])


#Words Lengths
print("************************Words length*********************")
fruits=["apple","banana","cherry","date"]
length_l=[]
for l in fruits:
length_l.append(len(l))
print(length_l)