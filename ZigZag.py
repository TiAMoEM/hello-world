# -*- coding:utf-8 -*-

def convert(self, s, numRows):
    if numRows == 1:
        return s
    ans = ''
    interval = 2 * (numRows - 1)
    for i in range(0, len(s), interval):
        interval = 2 * row
        i = row
        while i < len(s):
            ans += s[i]
            inter = interval - inter
            i += inter
    for i in range(numRows - 1, len(s), interval):
        ans += s[i]
    return ans




