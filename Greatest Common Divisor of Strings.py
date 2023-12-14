class Solution:
    def divisor(self, str1: str, str2: str):
        common_divisor = ''
        for i in range(min(len(str1), len(str2))):
            if str1[:i + 1] == str2[:i + 1]:
                common_divisor = str1[:i + 1]
            else:
                break
        return common_divisor
    
str1 = "ABAB"
str2 = "AB"
rozwiazanie = Solution()

result = rozwiazanie.divisor(str1, str2)
print(result)