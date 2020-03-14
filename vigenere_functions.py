def encodeVigenere(s, keyword):
    s = "".join([i for i in s.upper() if i.isalpha()])
    keyword = "".join([i for i in keyword.upper() if i.isalpha()])
    strInd = 0
    keywordInd = 0
    ans = ""
    while strInd < len(s):
        if ord(s[strInd]) - 65 + ord(keyword[keywordInd]) > 90:
            ans += chr(ord(s[strInd]) + ord(keyword[keywordInd]) - 91)
        else:
            ans += chr(ord(s[strInd]) - 65 + ord(keyword[keywordInd]))
        strInd+=1
        if keywordInd == len(keyword) - 1:
            keywordInd = 0
        else:
            keywordInd+=1
    return ans


def decodeVigenere(s, keyword):
    keyword = "".join([i for i in keyword.upper() if i.isalpha()])
    ans = ""
    strInd = 0
    keywordInd = 0
    while strInd < len(s):
        if ord(s[strInd]) - ord(keyword[keywordInd]) >= 0:
            ans += chr(ord(s[strInd]) - ord(keyword[keywordInd]) + 65)
        else:
            ans += chr(ord(s[strInd]) - ord(keyword[keywordInd]) + 91)
        strInd += 1
        if keywordInd == len(keyword) - 1:
            keywordInd = 0
        else:
            keywordInd += 1

    return ans


