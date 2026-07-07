import re
class Solution(object):
    def isPalindrome(self, s):
           cleaned_text=re.sub(r'[^a-zA-Z0-9]','',s)
           cleaned_text=cleaned_text.lower()
           return cleaned_text==cleaned_text[::-1]
s="A man, a plan, a canal: Panama"
sol=Solution()
sol.isPalindrome(s)