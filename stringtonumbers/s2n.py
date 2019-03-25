import re
from fractions import Fraction


# TODO: arg types and return types


def string_to_num(numeric_string):
    '''Convert numeric string to number
    
    Convert numeric strings to numbers accoding to their type, i.e. int, float, fraction.
    
    Args:
        numeric_string: A string which we want to convert. But for the reason of flexibility, a int or float is allowed to pass and will be returned directly.
    
    Returns:
        
    '''
     
    if isinstance(numeric_string, str):
    
        # Remove the thousands seperators, e.g. "255,000" --> "255000"
        numeric_string = numeric_string.replace(",","")
        
        # Convert string to Fractions
        if "/" in numeric_string:
            return Fraction(numeric_string)
    
        # Convert string to float
        elif "." in numeric_string:
            return float(numeric_string)
        
        # Convert string to int
        else:
               return  int(numeric_string)
    
    # If the type isn't str, we still do it a favor
    elif isinstance(numeric_string, int):
        return numeric_string
    elif isinstance(numeric_string, float):
        return numeric_string
    else: 
        raise ValueError("")

def extract_nums_from_string(string, number_word=False):
    '''
        TODO: Add 2e-6  number word   12/25 
    '''
    nums = re.findall(r'-?[1-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]+)?|\.[0-9]+', string)  # Ref: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch06s11.html
    nums = [string_to_num(n) for n in nums]
    
    return nums