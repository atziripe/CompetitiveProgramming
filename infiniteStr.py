def repeatedString(s, n):
    aperword = s.count("a")
    times = n // len(s)
    residuo = n % len(s)
    counter = (aperword*times)+s[:residuo].count("a")
    return counter
print(repeatedString("aba",7))
