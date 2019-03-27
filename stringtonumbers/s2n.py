import re
from fractions import Fraction





def to_num(numeric_string):
    '''Convert numeric string to number
    
    Convert numeric strings to numbers accoding to their type, i.e. int, float, fraction.
    
    Args:
        numeric_string: A string which we want to convert. But for ease of flexibility, a int or float input is allowed to pass and will be returned directly.
    
    Returns:
        A int, float or Fraction which is converted from the input string.
        
    Raises: 
        ValueError: If the input isn't a string, int or float, it will raise a ValueError("Invalid numeric input!"). If the input is a string with invalid character, it will raise a ValueError("Invalid numeric string!")
    '''
     
    if isinstance(numeric_string, str):
    
        # Preprocess - remove the thousands seperators, e.g. "255,000" --> "255000"
        numeric_string = numeric_string.replace(",","")
        
        # Convert strings to nums
        try:
            if "/" in numeric_string:  # Convert to Fractions
                return Fraction(numeric_string)
            elif "." in numeric_string: # Convert to float
                return float(numeric_string)
            else: # Convert to int
                return  int(numeric_string)
        except ValueError:
                raise ValueError("Invalid numeric string!")
                
    # If the type isn't str, we still do it a favor
    elif isinstance(numeric_string, int):
        return numeric_string
    elif isinstance(numeric_string, float):
        return numeric_string
    else: 
        raise ValueError("Invalid numeric input!")

        
        
        
        
        
def get_nums(string, return_string=False):
    '''
    
        Ref: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch06s11.html
    '''
    nums = re.findall(r'-?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?|\.[0-9]+', string)  # Ref: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch06s11.html
    
    if return_string:
        return nums
    else:
        nums = [to_num(n) for n in nums]
    
    return nums