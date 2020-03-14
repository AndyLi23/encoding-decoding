def encodeBase64(str):
    def to64(binStr):
        intVal = int(binStr, 2)
        if (intVal <= 25):
            return chr(intVal + 65)
        elif (intVal <= 51):
            return chr(intVal + 71)
        elif (intVal <= 61):
            return chr(intVal - 4)
        elif (intVal == 62):
            return "+"
        else:
            return "/"

    b = "".join(["".join("0" for i in range(8-len(bin(ord(char))[2:]))) + bin(ord(char))[2:] for char in str])
    s = [b[0+i:6+i] for i in range(0, len(b), 6)]
    e = 0

    if len(s[-1]) != 6:
        e = (6 - len(s[-1])) // 2
        s[-1] += "".join("0" for i in range(6-len(s[-1])))

    return "".join([to64(i) for i in s]) + "".join("=" for i in range(e))


def decodeBase64(str):
    s = ""

    for char in str:
        o = ord(char)
        if 65 <= o <= 90:
            s += "".join("0" for i in range(6-len(bin(o - 65)[2:]))) + bin(o - 65)[2:]
        elif 97 <= o <= 122:
            s += "".join("0" for i in range(6-len(bin(o - 71)[2:]))) + bin(o - 71)[2:]
        elif 48 <= o <= 57:
            s += "".join("0" for i in range(6-len(bin(o + 4)[2:]))) + bin(o + 4)[2:]
        elif o == 43:
            s += "".join("0" for i in range(6-len(bin(62)[2:]))) + bin(62)[2:]
        elif o == 47:
            s += "".join("0" for i in range(6-len(bin(63)[2:]))) + bin(63)[2:]

    return "".join([chr(int(i, 2)) for i in [s[0+i:8+i] for i in range(0, len(s), 8)] if len(i) == 8])

