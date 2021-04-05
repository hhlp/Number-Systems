import os

class Binary_Calculator_v2(object):
    def __init__(self, string_length):
        self.string_length = string_length
        self.binary_array = self.binary_string()
        self.digit_array = self.calculate_bin_str()
        self.added_bytes = sum(self.digit_array)


    """ Populate the binary string """
    def binary_string(self):
        bin_str = [0 for i in range(self.string_length)]    # Populate binary string with 0's
        for index in range(self.string_length):
            os.system("cls")
            print("[ Binary Calculator ]\n")
            print(f"Current Binary String:  {bin_str}")
            try:
                value = int(input(f"Enter {index+1} element (0 - 1) Left to Right: "))
                if value == 0 or 1:
                    bin_str[index] = value
                else:
                    print("Need binary 0 - 1...")
                    break
            except:
                print("Need Integer values, 0 - 1")

        print(f"Current String: {bin_str}")
        return bin_str
    

    """ Calculates each respectable bit's value and assign it to the "binary_string" """
    def calculate_bin_str(self):
        binary_string = list(reversed(self.binary_array))  # Revert the list so we calculate from right to left
        calculated = []
        for index, value in enumerate(binary_string):
            if value == 1:
                value += 1
                calculated.append(value**index)
            elif value == 0:
                calculated.append(0)
            else:
                print("Can only take binary numbers (0-1)")
                break
        return list(reversed(calculated))


    def __repr__(self):
        os.system("cls")
        print("[ Binary Calculator ]\n")
        print(f"Binary String:  {self.binary_array}")
        print(f"Digit String:  {self.digit_array}")
        print(f"Total Amount of Bits:  {self.added_bytes}")
        return str("Program Exited...")


if __name__ == "__main__":
    os.system("cls")
    print("[ Binary Calculator ]\n")
    string_length = int(input("Enter length of binary string\n  >> "))
    print(Binary_Calculator_v2(string_length))

