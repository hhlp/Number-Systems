import os
import re
import sys
import time
from BinaryToDecimal import BinaryToDecimal
from DecimalToBinary import DecimalToBinary
from BinaryToDecimal import BinaryToDecimal
from DecimalToHex import DecimalToHex
from HexToDecimal import HexToDecimal

base_menu = str("""
    [ Number System Converter ]
[0] Exit.
[1] Binary.
[2] Hexadecimal.
""")


def base_selection():
    bases = {
        "0": sys.exit,
        "1": binary,
        "2": hexadecimal
    }
    while True:
        os.system("cls")
        print(base_menu)
        print("[ Base Selection ]")
        try:
            choice = str(int(input("  >> ")))
            if -1 > int(choice) > 2:
                print("Please enter a number between 0 and 2")
                time.sleep(2)
                continue
        except TypeError:
            print("Please enter a number")
            time.sleep(2)
            continue
        method = bases[choice]
        return method()
        

# def base_test(convert_me):
#     bins = {"0", "1"}
#     base_string = set(convert_me)
#     if bins == base_string or base_string == {"0"} or base_string == {"1"}:
#         return "Binary"
#     elif re.fullmatch(r"^[A-F0-9]$", convert_me):
#         return "Hexadecimal"
#     else:
#         return "Decimal"
    

def binary():
    methods = {"0": base_selection,
               "1": BinaryToDecimal,
               "2": DecimalToBinary}
    while True:
        os.system("cls")
        print("[ Binary Convertion ]\n\n[0] Back\n[1] Convert Binary\n[2] Convert Decimal\n\n")
        try:
            choice = str(int(input("  >> ")))
            if -1 > int(choice) > 2:
                print("Please enter a number between 0 and 2")
                time.sleep(2)
                continue
        except TypeError:
            print("Please enter a number")
            time.sleep(2)
            continue
        
        method = methods[choice]
        
        if method == base_selection:
            return base_selection()
        
        elif method == BinaryToDecimal:
            while True:
                os.system("cls")
                print("[ Binary to Decimal Convertion ]\nEnter Binary:")
                try:
                    convert_me = int(input("  >> "))
                    result = BinaryToDecimal(str(convert_me))
                except:
                    print("Enter a binary string please..")
                    time.sleep(2)
                    continue
                return print(result)
        
        elif method == DecimalToBinary:
            while True:
                os.system("cls")
                print("[ Decimal to Binary Convertion ]\nEnter Decimal:")
                try:
                    convert_me = int(input("  >> "))
                    result = BinaryToDecimal(str(convert_me))
                except:
                    print("Enter a binary string please..")
                    time.sleep(2)
                    continue
                return print(result)
            
#     if base_test(convert_me) == "Binary":
#         print("Binary number detected!")
#         # print(BinaryToDecimal(convert_me))
#     else:
#         print("Decimal number detected!")
#         # print(DecimalToBinary(convert_me))

def hexadecimal():
    os.system("cls")
    print("[ Hexadecimal Convertion ]\n")
#     print("Please enter your hexadecimal-string or number sequence:")
#     convert_me = input("  >> ").upper()
#     if base_test(convert_me) == "Hexadecimal":
#         print("Hexadecimal number detected!")
#         # print(BinaryToDecimal(convert_me))
#     else:
#         print("Decimal number detected!")
#         # print(DecimalToBinary(convert_me))


if __name__ == "__main__":
    base_selection()
    