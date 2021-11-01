class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        length = len(s)
        LIMIT = 2 ** 31
        isNeg = -1
        i = 0
        if s[0] == '-':
            isNeg = 1
            i = 1
        elif s[0] == '+':
            isNeg = 0
            i = 1
        elif s[0].isdigit():
            isNeg = 0
            i = 0
        else:
        #elif not s[0].isdigit():
            return 0
        tempString = ''
        if i >= length:
            return 0
        if not s[i].isdigit() and i < length:
            return 0
        while s[i].isdigit():
            tempString += s[i]
            i += 1
            if i >= length:
                break
        if int(tempString) > LIMIT and isNeg:
            return 0-LIMIT
        elif int(tempString) > LIMIT-1 and not isNeg:
            return LIMIT-1

        else:
            if isNeg:
                return 0 - int(tempString)
            else:
                return int(tempString)
