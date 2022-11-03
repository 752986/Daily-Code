# pyright: strict


def isPalindrome(s: str) -> bool:
	length = len(s)
	for i in range(length // 2):
		if s[i] != s[length - i - 1]:
			return False
	return True


while True:
	a = input("> ")
	print(isPalindrome(a))
