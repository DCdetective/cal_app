from cal_fuc import addition,subtraction
def main():
    print("Welcome")
    print("""
    Select which operation do you want to do:
    1. Addition
    2. Subtraction
    """)

    option = input("Enter your desired option : ")

    a = int(input("Enter the number a : "))
    b = int(input("Enter the number b : "))

    if option == "1":
        return print(addition(a,b))
    elif option == "2":
        return print(subtraction(a,b))
    else:
        print("Option is invalid")

main()
