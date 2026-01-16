#set operations
set_1={1,2,3,4,5}
set_2={4,5,6,7,8,9}
set_3=set_1.union(set_2)

print("*******************************union***************************")

print(set_3)
print("****************************difference**********************")
set_4=set_1.difference(set_2)
print(set_4)

print("*******************Intersection*********************")
set_5=set_1.intersection(set_2)
print(set_5)

print("*******************Symmetric difference********************")
set_6=set_1.symmetric_difference(set_2)
print(set_6)

print("***********************is disjoint***************************")
set_7=set_1.isdisjoint(set_2)
print(set_7)

print("**********************subset/super set*******************")
set_10={1,2,3,4,5}
set_20={1,2,3,4,5}
set_30={1,2,3,4,5}
set_40={1,2}
print(set_10.issuperset(set_20))
print(set_30.issuperset(set_40))
print(set_40.issubset(set_30))

print("*************************frozen set*********************")

set_40={1,2}
set_40.add("python life")
print(set_40)
set_50=frozenset(set_40)
print(set_50)

#coding exercise
#Task 1:Set Intersection
print("Task 1:Set Intersection")
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set.intersection(set2)
print(set3)

#Task 2:Set Union
print("Task 2:set union")
set4=set1.union(set2)
print(set4)

#Task 3:Set Difference
print("Task 3:Set Difference")
set5=set1.difference(set2)
print(set5)

#Task 4:Set Symmetric Difference
print("Task4:Set Symmetric Difference")
set6=set1.symmetric_difference(set2)
print(set_6)

#Task 5:Set Membership Test
my_set={1,2,3,4,5}
print(3 in my_set)


#Tuples
print("*******************Tuples**********************")
tuple=()
print(tuple)
print(type(tuple))

personal_info=("devi","divya","sai",2,5,6,7,9.3)
print(f"Tuple length is {len(personal_info)}") #len
print(personal_info[1]) #index
print(personal_info[1:])

print(personal_info.count(3))#count

tuple1=(1,2,3)
tuple2=("a","b","c")
tuple3=tuple1+tuple2 #concatenation
print(tuple3)


#membership operators
fruits=("apple","banana")
is_apple="apple"in fruits
print(is_apple)

number=(1,2,3)
repeat_num= number * 2
print(repeat_num)
print("-"*10)


#Write a Python program to generate a bill for a super market purchase.
''''''
#item price
#___________________________
#apple 50

#banana 40

#milk 10

#__________________________
#total 100
''''''

items=[("apple",50),("banana",40),("milk",10)]

print(f"Item\t price")
print("-"*20)
total=0
for i,j in items:
    print(f"{i}\t{j}")
    total+=j
    print("_"*20)
    print(f"total\t{total}")


    #coding Exercise:
    print("Coding Exercise:")
    #Create a Tuple
    #1 Write a program that creates a tuple contains three
    #elements:your name,your age and your favourite colour.Then print tuple
    print("Create a tuple")
    tuple4=("devi",35,"green")
    print(tuple4)

    #Access Tuple Elements Write a program that creates a tuple containing the 
    #days of the week.Then,print the third element of the tuple.
    print("#Access Tuple Elements")
    days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    print(days[2])


    #Tuple Concatenation Write a program that creates two tuples,one
    #containing odd numbers from 1 to 5 and another containing even numbers
    #from 2 to 6 concatenate these two tuples and print result
    print("Tuple Concatenation")
    odd_numbers=(1,3,5)
    even_numbers=(2,4,6)
    result=odd_numbers+even_numbers
    print(result)

    #Tuple Unpacking Write a program that defines a tuple containing the
    #dimensions of a rectangle (lrngth and width).Then,unpack this tuple into
    #two variables and calculate the area of the rectangle
    print("Tuple Unpacking")
    dimensions=(10,5)
    length,width=dimensions
    area=length*width
    print("Area of the rectangle:",area)

    #Check if an Element Exists Write a program that checksif a given element 
    #exixts in a tuple


    numbers=(10,20,30,40,50)
    print(10 in numbers)

    #Write  a Python program to generate a bill for a supermarket purchase.The program should store the items and 
    #their prices in a list of tuples.It should then iterate over this list to print out each item along with its
    #price.Finally,  calculate and print the total cost of all the item
    print("super market purchase")
    print("                ")
    items=[("apple",100),("banana",100),("milk",50)]
    print(f"Item\tprice")
    print("-"*20)
    total=0
    for i,j in items:
        print(f"{i}\t{j}")
        total+=j
        print("_",20)
        print(f"total\t{total}")


#Project
#Supermarket Billing System

print("========================================================")
print("         WELCOME TO SUPER MARKET ")
print("=========================================================")

#Ask customer name
customer_name=input("Enter your name:").strip()
print(f"\nHello{customer_name},welcome to Super Mart!\n")

#product catalog
products={
    "Rice":50,
    "milk":50,
    "Bread":40,
    "Eggs":7,
    "Sugar":50,
    "oil":140,
    "Tea": 100
}

#Display products
print("Available products")
print("----------------------------------------------")
for item,price in products.items():
    print(f"{item:<10}-Rs{price}")
    print("--------------------------------\n")

    cart={}


    While True:
    choice=input("Do you want to buy something?(yes/no):").strip().lower()

    if choice=="no":
        break
    elif choice!="yes":
        print("Invalid choice,please type yes or no. \n")
        continue

    product=input("Enter the product name:").strip()

    #validate product
    if product not in products:
        print("Product not availabe!Please choose from the list.\n")

continue

#Enter quantity
qty=int(qty)


#Add to cart
if product in cart:
    cart[product]+=qty
else:
    cart[product]=qty

    print(f"Added{qty} x {product} to your cart .\n")

    #Generate Bill
    print("\n\n===========================================================")
    print("               SUPER MART BILL                      ")

    print("===================================================================")
    print(f"Customer Name:{customer_name}")
    print("Location    :Hyderabad")
    print("----------------------------------------------------------------------------")
    print(f"{'Item':<10}{'Qty':<5}{'price':<8}{'Total':<10}")
    print("---------------------------------------------------------------------------------")

    total_before_tax=0

    for item,qty in cart.items():
        price=products[item]
        total=price * qty
        total_before_tax+=total
        print(f"{item:<10}{qty:<5} Rs {price:<6} Rs{total:<10}")

        print("--------------------------------------------------------------------------------")
        print(f"Subtotal:Rs {total_before_tax:.2f}")

        tax=total_before_tax * 0.12
        print(f"Tax(12%): Rs{tax:.2f}")
         

        total_after_tax=total_before_tax + tax
        print(f"Total amount: Rs{total_after_tax:.2f}")

        print("------------------------------------------------------------------------")
        print("         THANK YOU FOR SHOPPING WITH US!             ")
        print("==================================================================================")