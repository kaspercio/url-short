class UrlManager:    
        
        def __init__(self, input: str, link: str, python_dict: dict):
                self.input = input
                self.base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                self.link = link
                self.python_dict = python_dict

        def encode(self):
                output = ""
                quotient = self.input
                while(quotient > 0):
                        remainder = quotient % 62
                        quotient = quotient // 62
                        output = output + self.base62[remainder]
                output = output[::-1]
                output = str(output)
                print(output)
                self.python_dict[output] = self.link
                return self.python_dict
        
        def decode(self):
                output = ""
                
                # find the character at the end index of the encoded number from the base62 string
                # convert it to an integer. 
                output = str(self.input)
                return output

                