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
        print("[ Base Selection ]:")
        try:
            choice = int(input("  >> "))
            if choice < -1 or choice > 2:
                print("Please enter a number between 0 and 2")
                time.sleep(2)
                continue
            else:
                method = bases[str(choice)]
                return method()
        except TypeError:
            print("Please enter a number")
            time.sleep(2)
            continue


def base_test(convert_me):
    bins = {"0", "1"}
    if set(convert_me) :
        return "Binary"
    elif re.fullmatch(r"^[0-9a-fA-F]$", convert_me):
        return "Hexadecimal"
    elif re.fullmatch(r"[0-9]$", convert_me):
        return "Decimal"
    

def binary():
    print("\n\n[ Binary Convertion ]")
    print("Please enter your bit-string or number sequence:")
    convert_me = input("  >> ")
    if base_test(convert_me) == "Binary":
        print("Binary number detected!")
        # print(BinaryToDecimal(convert_me))
    else:
        print("Decimal number detected!")
        # print(DecimalToBinary(convert_me))


def hexadecimal():
    print("\n\n[ Hexadecimal Convertion ]")
    print("Please enter your hexadecimal-string or number sequence:")
    convert_me = input("  >> ").upper()
    if base_test(convert_me) == "Hexadecimal":
        print("Hexadecimal number detected!")
        # print(BinaryToDecimal(convert_me))
    else:
        print("Decimal number detected!")
        # print(DecimalToBinary(convert_me))


if __name__ == "__main__":
    base_selection()
    