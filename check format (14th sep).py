import math
from typing import Union

def _wordform_threedigit(number: int) -> str:
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] # digit -> bridget -> brisket <3
    tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    string = str(number)
    if len(string) > 3:
        raise ValueError("more than three digits provided")
    elif len(string) < 1:
        raise ValueError("not enough digits provided")

    output = ""

    teens = False
    if len(string) == 3: # there is a hundreds place
        output += digits[int(string[0])] + " hundred "
    if len(string) >= 2:
        lasttwo = int(string[len(string)-2:len(string)]) # value of last two digits
        if lasttwo < 20: # handle "*-teen"s
            teens = True
            output += digits[lasttwo]
        else: # tens place
            output += tens[int(string[len(string)-2])] + ("-" if string[len(string)-1] != "0" else "")
    if not teens: # ones place
        output += digits[int(string[len(string)-1])]

    if output != "":
        output += " "

    return output


def wordform(number: Union[float, int]) -> str:
    places = ["", "thousand", "million", "billion", "trillion"]

    if number <= 0: # zero or negative
        raise ValueError("the supplied number was too small")
    elif number >= 1_000_000_000_000_000: # quadrillion or more, don't have a string for it
        raise ValueError("the supplied number was too big")

    output = ""

    string = str(round(number, 2))
    print(string)
    whole = string.split(".")[0]

    if whole == "0":
        output += "zero "
    else:
        for i, place in enumerate(whole[0:len(whole):3]):
            power = places[math.floor(len(whole) / 3) - i]
            amount = _wordform_threedigit(int(place)) + power
            output += amount
            # TODO: fix space getting added
            #output += " " if amount != "" else ""

    fractional = string.split(".")[1] if "." in string else ""
    if fractional not in ["", "0"]:
        if len(fractional) == 1:
            fractional += "0"
        if fractional[0] == "0":
            fractional = fractional[1]
        output += " and {} / 100 ".format(fractional)

    output += "dollars"

    return output

while True:
    response = input("Enter a number (`exit` to quit): \n> ").strip()
    if response in ["exit", "quit"]:
        break

    number: Union[int, float]

    try:
        number = float(response)
    except ValueError:
        print("Invalid input, try again")
        continue

    try:
        print(wordform(number))
    except ValueError:
        print("Invalid input, try again")
        continue