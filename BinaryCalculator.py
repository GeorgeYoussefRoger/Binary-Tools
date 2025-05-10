def menu1():
    print("=== Welcome to the binary calculator ===")
    choice = input("Choose:\nA) Insert a number\nB) Exit the program\n")
    global num
    if choice == "A" or choice == "a":
        num = (input("Enter a binary number: "))
    elif choice == "B" or choice == "b":
        print("Exiting")
        exit()
    else:
        print("Enter a valid choice")
        return menu1()
    checker = True
    for i in num:
        if i not in {"0", "1", "-"}:
            checker = False
    if checker == False:
        print("Enter a valid number")
        menu1()
    else:
        num = str(num)
        menu2()

def num2():
    global num2
    num2 = (input("Enter the second binary number: "))
    checker = True
    for i in num2:
        if i not in {"0", "1","-"}:
            checker = False
    if checker == False:
        print("Enter a valid number")
        menu2()
    else:
        return int(num2)

def menu2():
    print("Choose an operation:")
    operation = input("a)Compute one's complement\nb)Compute two's complement\nc)Addition\nd)Subtraction\n")
    if operation == "a" or operation == "A":
        num1 = str(num)
        binary_to_first_complement(str(num1))
    elif operation == "b" or operation == "B":
        num1=str(num)
        binary_to_second_complement(str(num1))
    elif operation == "c" or operation == "C":
        num2()
        addition(str(num), str(num2))
    elif operation == "d" or operation == "D":
        num2()
        subtraction(str(num), str(num2))
    else:
        print("Enter a valid choice")
        return menu2()
    menu1()

# Function to compute one's complement
def binary_to_first_complement(binary_num):
    if binary_num[0] == "-":
        binary_num = binary_num[1:]
    firstcomplment = ""
    for char in binary_num:
        if char == "0":
            firstcomplment += "1"
        else: 
            firstcomplment += "0"
    print("the first complement is", firstcomplment )

# Function to compute two's complement
def binary_to_second_complement(binary_num):
    if binary_num[0] == "-":
        binary_num=reversed(binary_num[1:])
    second_complement = bin(binary_num + 1)[2:]
    print("the second complement is", second_complement)

# Function to add two binary numbers
def addition(a, b):
    global num
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ""
    temp = 0
    for i in range(max_len - 1, -1, -1):
        num = int(a[i]) + int(b[i]) + temp
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        if num == 2:
            temp = 1
        else:
            temp = 0
    if temp != 0:
        result = "01" + result
    print("The result is", result)

# Function to subtract two binary numbers
def subtraction(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ""
    temp = 0
    for i in range(max_len - 1, -1, -1):
        num = int(a[i]) - int(b[i]) - temp
        if num % 2 == 1:
            result = "1" + result
        else:
            result = "0" + result
        if num < 0:
            temp = 1
        else:
            temp = 0     
    if temp != 0:
        result = "01" + result
    print("The result is", result)

menu1()