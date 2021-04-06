import os
import sys
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
    print(base_menu)
    print("[ Base Selection ]:")
    try:
        choice = str(int(input("  >> ")))
        if -1 > choice > 2:
            print("Please enter a number between 0 and 2") 
    except TypeError:
        print("Please enter a number")
    method = bases[choice]
    return method()


def binary():
    print("\n\n[ Binary Convertion ]")
    print("Please enter your bit-string or number sequence:")
    convert_me = input("  >> ")
    for num in convert_me:
        if num in str(range(2, 9)):
            print("Decimal Input!")
            # print(DecimalToBinary(convert_me))
        else:
            print("Binary Input!")
            print(BinaryToDecimal(convert_me))


def hexadecimal():
    print("[ Hexadecimal Convertion ]")
    print("Please enter your hexadecimal-string or number sequence:")
    convert_me = input("  >> ")


if __name__ == "__main__":
    base_selection()
    