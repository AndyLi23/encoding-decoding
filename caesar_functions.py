def encodeCaesar(str, n):
    str = [i for i in str.upper() if i.isalpha()]
    ans = ""
    for i in str:
        if ord(i) + n > 90:
            ans += chr(64 + (ord(i)+n) % 90)
        else:
            ans += chr(ord(i) + n)
    return ans

def decodeCaesar(str, n):
    str = [i for i in str.upper()]
    ans = ""
    for i in str:
        if ord(i) - n < 65:
            ans += chr(90-(64 - (ord(i) - n)))
        else:
            ans += chr(ord(i) - n)
    return ans


