# Numbers from String


This Python module provides functions that get the numbers or the numeric string tokens in an input string. 

To capture the numerals in a piece of text is a common preprocess for retrieving numerical information from documents. However, due to the various representations of these numerals, it's somewhat tricky to capture them all using simple  rules. We packed several regex rules with comprehensive coverage in this library and hope it can be a useful tool for NLP researchers.


## Installation
```
```

## Usage


1. Extract numbers from a string
```python
>>> string1 = "U.S. goods and services trade with China totaled an estimated $710.4 billion in 2017. "
>>> nums_from_string.get_nums(string1)
[710.4, 2017]

>>> string2 = "David spent .25 billion dollars buying a building and 600,000.5 dollars getting himself a car."
>>> nums_from_string.get_nums(string2)
[0.25, 600000.5]

```

2. Extract numeric strings from a string
```python
>>> string1 = "U.S. goods and services trade with China totaled an estimated $710.4 billion in 2017. "
>>> nums_from_string.get_numeric_string_tokens(string1)
['710.4', '2017']

>>> string2 = "David spent .25 billion dollars buying a building and 600,000.5 dollars getting himself a car."
>>> nums_from_string.get_numeric_string_tokens(string2)
['.25', '600,000.5']

```


3. Convert strings to numbers
```python
>>> s0 = "255"
>>> nums_from_string.to_num(s0)
255

>>> s1 = "-255,000.0"
>>> nums_from_string.to_num(s1)
-255000.0

>>> s2 = "87/25"
>>> nums_from_string.to_num(s2)
Fraction(87, 25)

>>> s3 = "a1b2"
>>> nums_from_string.to_num(s3)
Traceback (most recent call last):
    ...
ValueError: Invalid numerical string!

```



## Todo
- [ ] 把usage搬過去
- [ ] unit test寫好
- [ ] 把負號關掉
- [ ] 抓 fraction
- [ ] "-3.5/11"



## Reference
