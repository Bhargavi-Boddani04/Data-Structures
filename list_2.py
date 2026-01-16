#list
print("************List*******************")


list=[]
print(list)
print(type(list))

list_2=[28,4.5,"Python life",(2,4,5),{6,9,8},[2,6,9],5,5,5,5]
print(list_2)
print(type(list_2))
list_3=list
print(list_3)


#accessing individual elements
print("**************acecessing individual elements******************")


list_1=[10,20,30,40,50,60,70,80,90]
list_1[4]
print(list_1)
print(list_1[4])

#slicing
print("**************Slicing*********************")
print(list_1[1:5])
print(list_1[0:2])
print(list_1[::1])
print(list_1[::2])
print(list_1[::3])
print(list_1[5:3:-1])
print(list_1[5::-1])
print(list_1[::-1])
print(list_1[:2:-1])

#Nested list
print("***************Nested list**********************")
matrix=[[1,2,5],[6,8,9],[4,5,1]]
print(matrix[2][1])


