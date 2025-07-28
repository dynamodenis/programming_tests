def findAnagrams(s: str, p: str):
    if len(p) > len(s):
        return []

    pCount, sCount = {}, {}

    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    res = []
    if sCount == pCount:
        res.append(0)

    l = 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        sCount[s[l]] -= 1

        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        l += 1

        if sCount == pCount:
            res.append(l)

    return res


response = findAnagrams("cbaebabacd", "abc")


def isAnagram(s: str, t: str):

    if len(s) != len(t):
        return False
    sCount, tCount = {}, {}
    for i in range(len(s)):
        sCount[s[i]] = 1 + sCount.get(s[i], 0)
        tCount[t[i]] = 1 + tCount.get(t[i], 0)

    # if sCount != tCount:
    #     print(f"IS Not ANOGRAM")
    #     return False

    for c in sCount:
        if sCount[c] != tCount.get(c, 0):
            return False

    return True


response = isAnagram("abc", "bca")
