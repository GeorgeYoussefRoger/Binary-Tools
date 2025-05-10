def menu1():
    print("=== Welcome to the number conversion program ===")
    choice =  input("Choose:\nA) Insert a number\nB) Exit the program\n")
    global num1
    if choice == "A" or choice == "a":
        num1=input("Enter a number: ")
        menu2(num1)                
    elif choice == "B" or choice == "b":
       print("Exiting")
       exit()
    else :
       print("Enter a valid choice")
       return menu1()

def menu2(num):
    global base_from
    print("Please select a base you want to convert from:")
    print("Choose:")
    base_from= input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\n")
    if base_from != "a" and base_from != "A" and base_from != "b" and base_from != "B" and base_from != "c" and base_from != "C" and base_from != "d" and base_from != "D":
        print("Enter a valid choice")
        return menu2(num)
    else: 
        menu3(num, base_from)

def menu3 (mainnumber, input_base):
    global base_to
    print("Select a base you want to convert to:")
    base_to = input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\n")
    if base_to!= "a" and base_to != "A" and base_to != "b" and base_to != "B" and base_to != "c" and base_to != "C" and base_to != "d" and base_to != "D":
        print("Enter a valid choice")
        return menu3(mainnumber, input_base)
    elif input_base == "b" and base_to == "a":
        bin_dec(int(mainnumber))
    elif input_base == "a" and base_to == "b":
        dec_bin(int(mainnumber))
    elif input_base == "c" and base_to == "a":
        oct_dec(int(mainnumber))
    elif input_base == "a" and base_to == "c":
        dec_oct (int(mainnumber))
    elif input_base == "a" and base_to == "d":
        dec_hex(int((mainnumber)))
    elif input_base == "d" and base_to == "a":  
        hex_dec(mainnumber)
    elif input_base == "b" and base_to == "c":
        dec_oct(bin_dec(int(mainnumber)))
    elif input_base=="b" and base_to=="d":
        dec_hex(bin_dec(int(mainnumber)))
    elif input_base=="d" and base_to=="c":
        dec_oct(hex_dec(mainnumber))
    elif input_base=="d" and base_to=="b": 
        dec_bin(hex_dec((mainnumber)))
    elif input_base=="c" and base_to=="d":
        dec_hex(oct_dec(int(mainnumber)))
    elif input_base=="c" and base_to =="b":
        dec_bin (oct_dec(int(mainnumber))) 
    menu1()
        
       
# Function to convert binary to decimal      
def bin_dec(bin_num):
     dec = 0
     i = 0
     while bin_num > 0:
        remainder = bin_num % 10
        exp = remainder * (2**i)
        dec = dec + exp
        bin_num = bin_num // 10
        i += 1
     print("the decimal number is", dec)

# Function to convert decimal to binary
def dec_bin(dec_num):
    bin = ""
    while dec_num > 0:
        rem = dec_num % 2
        bin = str(rem) + bin
        dec_num = dec_num // 2
    print("The binary number is", bin)
       
# Function to convert octal to decimal       
def oct_dec(oct_num):
    dec = 0
    i = 0
    while oct_num > 0:
        remainder = oct_num % 10
        exp = remainder * (8**i)
        dec = dec + exp
        oct_num = oct_num // 10
        i+=1
    print("the decimal number is", dec)

# Function to convert decimal to octal
def dec_oct(dec_num):
    oct = ""
    while dec_num > 0:
        rem = dec_num % 8
        oct = str(rem) + oct
        dec_num = dec_num // 8
    print("The octal number is", oct) 

# Function to convert decimal to hexadecimal
def dec_hex(dec_num):
    if dec_num == 0:
        return "0x0"
    hex = ""
    while dec_num > 0:
        remainder = dec_num % 16
        if remainder < 10:
            hex = str(remainder) + hex
        else:
            hex = chr(ord('A') + remainder - 10) + hex
        dec_num = dec_num // 16
    print("the hexadecimal number is", hex)

# Function to convert hexadecimal to decimal
def hex_dec(hex):
    hexadecimal = str(hex.strip().upper())
    table = {'0': 0, '1': 1, '2': 2, '3': 3,
             '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11,
             'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec = 0
    size = len(hexadecimal) - 1
    for num in hexadecimal:
        dec = dec + table[num]*16**size
        size = size - 1
    print("the decimal number is", dec)

menu1()