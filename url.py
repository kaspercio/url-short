class UrlManager:    
        
        def __init__(self, input: int):
                self.input = input
                self.base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        def encode(self):
                output = ""
                quotient = self.input
                while(quotient > 0):
                        remainder = quotient % 62
                        quotient = quotient // 62
                        output = output + self.base62[remainder]
                output = output[::-1]
                p_dict = {

                }
                string_input = str(self.input)
                p_dict[output] = string_input
                return p_dict
        
        