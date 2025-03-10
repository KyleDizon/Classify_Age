#Classify_Age
def age():
    age = int(input("Enter your age: "))
    if age < 0:
        print("Invalid Age! Please Enter Value Between 0 and 100")
    elif age <=12:
        print("You are a Child")
    elif age <=19:
        print("You are a Teen")
    elif age <64:
        print("You are a Adult")
    elif age >=65:
        print("You are a Senior")


age()

while True:
    a = input("Run again?: ")
    if a == "Yes":
        age ()
    
    else:
        b = print("Program Done")
        break