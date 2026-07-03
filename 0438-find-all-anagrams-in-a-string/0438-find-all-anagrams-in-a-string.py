from collections import Counter

class Solution:
    def findAnagrams(self, s, p):

        result = []

        p_count = Counter(p)

        window = Counter(s[:len(p)])

        if window == p_count:
            result.append(0)

        for i in range(len(p), len(s)):

            # Add new character
            window[s[i]] += 1

            # Remove old character
            window[s[i-len(p)]] -= 1

            if window[s[i-len(p)]] == 0:
                del window[s[i-len(p)]]

            if window == p_count:
                result.append(i-len(p)+1)

        return result
s="cbaebabacd"
p="abc"
k=Solution()
k.findAnagrams(s,p)
        