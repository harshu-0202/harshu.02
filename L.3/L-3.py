# print() formatting using  sep and end
# print("Apple" , "Banan" , "Cherry" , sep=" ," , end="<--- end of list\n")

#formatted message for user input

name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your hobby: ")

print(" my name is " + name + " and my age is " + age + " and hobby is " + hobby)

print(f"Hello , {name}! At {age} , enjoying {hobby} sounds fun! !")
