class BinaryConverter(object):
    def __init__(self, byte_string="11111111.11111111.11111111.11111111"):
        self.byte_string = byte_string
        
    def __str__(self):
        return str(self.byte_string)
    
    def __repr__(self):
        return str("Takes a bit string, splits it into bytes and converts it to decimal notation.")
    
if __name__ == "__main__":
    test = BinaryConverter()
    print(test)