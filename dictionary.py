#Dictionary
sample_dict={}
sample1_dict={1:"devi",2:"priya",3:"divya"}
empty_dict={}
print(sample_dict)
print(type(sample_dict))
print(sample1_dict)


print("***************************clear***********************")
empty_dict=sample1_dict
print(f"empty_dict{empty_dict}")
empty_dict.clear()
print(f"empty_dict{empty_dict}")

print("*******************************Copy**************************")
sample2_dict={1:"devi",2:"priya",3:"divya"}
empty_dict=sample2_dict.copy()
print(empty_dict)


print("*****************************Items************************")
dictionary_1={
    "user1":"user1@123",
    "user2":"user2@123",
    "user3":"user3@123"
}
print(dictionary_1.items())
print(dictionary_1.keys())
print(dictionary_1.values())

print("**********************update**********************")

dictionary_2={
    "user1":"user@123",
    "user2":"user@123",
    "user3":"user@123"
}

dictionary_3={
    "user4":"user@123",
    "user5":"user@123",
    "user6":"user@123"

}

print(dictionary_2)

dictionary_2.update(dictionary_3)
print(dictionary_2)

print("***************************gets*******************")

print(dictionary_2.get("user"))

print("**********************pop********************")

obj=dictionary_2.pop("user1")
print(obj)
print(dictionary_2)

#coding Exercise
print("********************Coding Exercise*********************")

#Write Python code to add a new key-value pair to the following dictionary
print("**************new key-value pair*********************")
my_dict={'name':'python','age':25}
my_dict['city']='West Godavari'
print(my_dict)

#Write Python code to access and print the value associated with the key 'price'
print("**************************Dictionary access***********************")
product_info={'name':'laptop','brand':'Dell','price':1200}
price_value=product_info['price']
print(price_value)

#Write Python code to remove the key-value pair with the key'city' from the
print("*******************Dictionary Removal********************")
my_dict={'name':'devi','age':'30','city':'tadepalligudem'}
my_dict.pop('city')
print(my_dict)

#Write Python code to print all the keys present in the following dictionary

print("******************Dictionary Keys*************************")
my_dict={'name':'python','age':'25','city':'Bhimavaram'}
keys_list=list(my_dict.keys())
print(keys_list)

#Write Python code to print all the values present in the following dictionary
print("************Dictionary values************************")
my_dict={'name':'python','age':'25','city':'rajahmundry'}
values_list=list(my_dict.values())
print(values_list)
