#sets
sample=()
print(type(sample))

sample1={1,5,4,7.0,"divya","priya"}
print(type(sample1))


print("****************************add************************")
sample1.add("pythonlife")
print(sample1)

print("******************copy**************************")
sample2=sample1.copy()
print(sample2)

print("************************pop**************************")
obj=sample2.pop()
print(obj)
print(sample2)

print("*****************remove***********************")
sample2.remove(4)
print(sample2)

#Mini project
print("*************************mini project*******************")

word_dict={}

while True:
    print("1.Add a Word")
    print("2.Search for Meaning")
    print("3.Display all words")
    print("4.Update Meaning")
    print("5.Delete Word")
    print("6.Exit")

    choice=input("Enter your choice(1-6):").strip()

    if choice=='1':
        #Add a word
        word=input("Enter the word to add:").strip()

        if word in word_dict:
            print(f"{word}'already exists with meaning:{word_dict[word]}")
        else:
            meaning=input(f"Enter the meaning of '{word}':").strip()
            word_dict[word]=meaning
            print(f"Word'{word}' added successfully")

    elif choice=='2':
        #search for meaning
        word=input("Enter the word to search:").strip()
        if word in word_dict:
            print(f"Meaning of '{word}':{word_dict[word]}")
        else:
            print(f"{word}'not found in the dictionary.")

elif choice=='3':
#Display all words
if word_dict:
    print("Dictionry Contents")
    for word,meaning in word_dict.items():
        print(f"{word}:{meaning}")
    else:
        print("The dictionary is empty")

elif choice=='4':
    #Update meaning
    word=input("Enter the word to update:").strip()
    if word in word_dict:
        new_meaning=input(f"Enter the new meaning for '{word}':").strip()
        word_dict[word]=new_meaning
        print(f"Updated meaning of '{word}':{word_dict[word]}")
    else:
        print(f"'{word}' not found in the dictionary.")

elif choice=='5':
    # Delete word
    word=input("Enter the word to delete:").strip()
    if word in word_dict:
        confirm=input(f"Are you sure you want to delete '{word}'?(yes/no:)").strip().lower()
        if confirm=='yes':
            del word_dict[word]
            print(f"'{word}' has been deleted.")
    else:
        print(f"'{word}' not found in the dictionary.")
elif choice=='6':
    print("Exist")
    break

else:
    print("Invalid input.Please enter a number between 1 and 6.")

