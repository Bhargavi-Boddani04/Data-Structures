#STRINGs
print("***********************STRINGS*************************")
single_quoted_string="Hello world"
print(single_quoted_string)
double_quoted_string="Hello world,time is 7'O clock"
print(double_quoted_string)
triple_quoted_string="Hello world, time is 7'O clock.plaese attend python life trining"
print(triple_quoted_string)
sample=""
print(sample)
print(type(sample))

sample_1=str()
print(type(sample_1))

#Index display
print("**********************Index dispaly********************")

str_1="Hello world"
print(str_1)
print(str_1[4])
print(str_1[-1])
print(str_1[6:8])
print(str_1[-7:-1])
print(str_1[-5:-7:-1])


#string methods
print("*******************string methods*********************")
print("*********************UPPERCASE********************")
message="Hello World"
print(message.upper())
print("****************LOWERCASE******************")
message="Hello World"
print(message.lower())

print("**************COUNT*************************")
message="Hello World"
print(message.count("W"))
sentence="Hello World"
count_1=sentence.count("W")
print(count_1)

print("***************************STRIP******************************")
whitespace="  This is my STRP program"
print(whitespace.strip())
print("*********************SPLIT************************")
data="pythonlife,bhargavi,23456"
data_1=data.split(',')
print(data_1)


print("****************************STARTS WITH ENDS WITH***************************")
filename='exampe.txt'
start_with=filename.startswith("ex")
print(start_with)
end_with=filename.endswith("xt")
print(end_with)


email_list=["bhagi@gmail.com","devi@gmail.com",divya@gmail.com]
empty_list=[]
for i in email_list:
    if i.endswith("@gmail.com"):
        empty_list.append(i)
        print(empty_list)

   print("**************find()Index()*********************")     

input_str='this is my program'
print(input_str.find('h'))
print(input_str.index('m'))
print(input_str.find('z'))

print("***********************is digit( is alpha()*******************")
numeric_string="1,2,3,4"
alpha_string="python"
is_numeric=numeric_string.isnumeric()
is_alpha=alpha_string.isalpha()
print(is_numeric)
print(is_alpha)

print("******************JOINS*************************")
word_list=["Hello world"]
joined_string='.join(word_list)'
print(joined_string)

print("********************F-STRING*********************************")
print(f"string joined {joined_string}")

print("***********************capitalized***********************")
input_str2="Python programming"
print(input_str2.capitalized())

#Coding Exercise
print("*************************coding exercise*************************")

print("**********************even indices***************************")
#you are given a string sentence.print the characters at even indices
sentence1="Python is amazing"
print(sentence1[0::2])
#Replace all spaces in the string with underscores_ and print the modified string
print("********************Replace******************")

print(sentence1.replace("","_"))

#Check if the string contains only digits
print("***************************digits******************************")
input_str_name=input("Enter input")
if any(ch.isdigit()for ch in input_str_name):
    print(f"string contains digits {input_str_name}")
else:
    print(f"string doesnot contain digits {input_str_name}")

    #print the string in reverse order.
    print("*************************Reverse order***********************")
    str_2="Python programming is fun"
    print(str_2[::-1])

    print("***************************capitalized**********************")
    input_str3="Python programming is fun"
    print(input_str3.capitalized())
    