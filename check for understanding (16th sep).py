def average(*nums: int | float) -> float:
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)

text = input("enter three numbers, separated by spaces: \n> ")
nums = [float(i) for i in text.replace(",", "").split()]
print(average(*nums))

######

def PythagoreanCheck(a: int, b: int, hypot: int) -> bool:
    return a**2 + b**2 == hypot**2

text = input("enter two sides and the hypotenuse, separated by spaces: \n> ")
nums = [int(i) for i in text.replace(",", "").split()]
if len(nums) != 3:
    raise ValueError("the number of arguements was not 3")
print(PythagoreanCheck(nums[0], nums[1], nums[2]))

######

# I already did the object stuff in week 1