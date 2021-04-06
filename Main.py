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
        "0": sys.exit(),
        "1": binary(),
        "2": hexadecimal()
    }
    print(base_menu)
    try:
        choice = str(int(input("  >> ")))
        if -1 > choice > 2:
            print("Please enter a number between 0 and 2") 
    except TypeError:
        print("Please enter a number")
    return bases[choice]


def binary():
    print("Binary selected")


def hexadecimal():
    print("Hexadecimal selected")

base_selection()


if __name__ == "__main__":
    print(base_selection())
    