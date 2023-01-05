import string
import time

# def crackany(search: str, max_depth: int = 4, n_chars = 1):
#     if n_chars > max_depth:
#         print("not found at depth {}".format(n_chars - 1))
#         return

#     for i in itertools.permutations(string.printable, n_chars): # this is cheating, and also doesn't work
#         current = "".join(i)
#         if current == search:
#             print("the password was {}!".format(current))
#             return current
    
#     return crackany(search, max_depth, n_chars + 1)

def crack(search: str, length: int) -> str | None:
    # this code was mostly stolen from kyle (thanks, kyle)
    chars = [ord(c) for c in search]
    check = [ord(" ") for _ in range(length)]

    while True:
        if chars == check:
            return "".join([chr(c) for c in check])

        check[0] += 1

        if check[-1] > 126: # we have searched all values and found nothing:
            return

        for i in range(length):
            if check[i] > 126: # this index is past the range of useful ascii values:
                check[i] = ord(" ")
                check[i + 1] += 1
                
def crackany(search: str, max_length: int = 4):
    for i in range(max_length):
        result = crack(search, i)
        if result != None:
            return result

while True:
    password = input("enter a password to find! (`exit` to quit) \n> ")

    if password == "exit":
        break

    starttime = time.process_time()

    print(crack(password, len(password)))

    print("(took {} seconds)".format(time.process_time() - starttime))