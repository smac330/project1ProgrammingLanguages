import re

def romanToInt(roman):
    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previousValue = 0
    
    for char in roman[::-1]:  #Start from the end of the Roman numeral string
        value = romanMap[char]
        if value < previousValue:
            result -= value
        else:
            result += value
        previousValue = value
    
    return result

def intToRoman(num):
    if num > 3999:
        return "You're going to need a bigger calculator."
    
    intMap = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    for value, numeral in intMap:
        while num >= value:
            result.append(numeral)
            num -= value
    return ''.join(result)

def replaceRoman(match):
    return str(romanToInt(match.group()))

def parseExpression(expression):
    try:
        #Convert Roman numerals in the expression to integers
        expression = re.sub(r'[IVXLCDM]+', replaceRoman, expression)

        #Handle parentheses and operator precedence using eval or custom parsing
        result = eval(expression)
        
        if result == 0:
            return "0 does not exist in Roman numerals."
        if result < 0:
            return "Negative numbers can't be represented in Roman numerals."
        if result % 1 != 0:
            return "There is no concept of a fractional number in Roman numerals."
        if result > 3999:
            return "You're going to need a bigger calculator."
        
        #Convert the integer result back to Roman numerals
        return intToRoman(int(result))
    except:
        return "I don't know how to read this."

if __name__ == "__main__":
    #Take input from the user instead of command line arguments
    inputExpression = input("Enter a Roman numeral expression: ")
    print(parseExpression(inputExpression))
