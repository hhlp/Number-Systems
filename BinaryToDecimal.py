class BinaryConverter(object):
    def __init__(self, bit_string="11111111.11111111.11111111.11111111"):
        self.bit_string = bit_string
        self.byte_list = bit_string.split(".")
        
    def __str__(self):
        return str(f"{self.bit_string}\n{self.convertion()}")
    
    def __repr__(self):
        return str("Takes a bit string, splits it into bytes and converts it to decimal notation.")
    
    def convertion(self):
        decimal_notation = ""
        for bit in self.byte_list:
            decimal_notation += str(int(bit, 2)) + "."
        last_dot = decimal_notation[-1]
        return decimal_notation.strip(last_dot)
    

if __name__ == "__main__":
    test = BinaryConverter()
    print(test)