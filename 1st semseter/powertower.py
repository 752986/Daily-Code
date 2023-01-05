for n in range(20):
    s = "print("
    for i in range(n):
        s += "10" + ("**" if i != n - 1 else "")

    s += ")"

    eval(s)