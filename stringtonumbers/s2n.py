import re
from fractions import Fraction




def to_num(numerical_string):
    '''Convert numerical string to number
    
    Convert a numerical string to a number accoding to its type, i.e. int, float, fraction.
    
    Args:
        numerical_string: A string which we want to convert. But for ease of flexibility, a int or float input is allowed to pass and will be returned directly.
    
    Returns:
        A int, float or Fraction which is converted from the input string.
        
    Raises: 
        ValueError: If the input isn't a string, int or float, it will raise a ValueError("Invalid  input type!"). If the input is a string with invalid character, it will raise a ValueError("Invalid numerical string!")
    '''
     
    if isinstance(numerical_string, str):
    
        # Preprocess - remove the thousands seperators, e.g. "255,000" --> "255000"
        numerical_string = numerical_string.replace(",","")
        
        # Convert strings to nums
        try:
            if "/" in numerical_string:  # Convert to Fractions
                return Fraction(numerical_string)
            elif "." in numerical_string: # Convert to float
                return float(numerical_string)
            else: # Convert to int
                return  int(numerical_string)
        except ValueError:
                raise ValueError("Invalid numerical string!")
                
    # If the type isn't str, we still do it a favor for ints and floats
    elif isinstance(numerical_string, int):
        return numerical_string
    elif isinstance(numerical_string, float):
        return numerical_string
    else: 
        raise ValueError("Invalid input type!")




def get_numerical_string_tokens(string):
    ''' Get the numerical string tokens in a string.
    
    This function uses regular expression to match numerical string tokens in a string.
    The "-?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?" pattern matches strings like "25", "-25", "125,000,000", "0.25"
    , while the "\.[0-9]+" pattern matches numbers like ".25", ".12"
    Ref: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch06s11.html
    
    Args:
        string: A string which we want to find the numerical strings.
        
    Returns:
        tokens: A list of string of the targeted numerical string tokens 
    '''
    tokens = re.findall(r'-?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?|\.[0-9]+', string)  
    return tokens

        
        
        
def get_nums(string):
    ''' Get numbers from a string.
    
    This function uses regular expression to match numerical string tokens in a string, and convert them to numbers according to their types.
    
    Args:
        string: A string from which we want to find numbers.
        
    Returns:
        nums: A list of ints or floats  or a mixture of them which consists of the numbers we extract from the input string. 
    '''
    
    tokens = get_numerical_string_tokens(string)
    nums = [to_num(t) for t in tokens]
    return nums