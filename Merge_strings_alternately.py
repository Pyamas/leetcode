class Solution: 
    def mergAlternately(self, word1: str, word2:str) -> str:
        return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):]

word1 = 'abcd'
word2 = 'pq'
solution_instance = Solution()
result = solution_instance.mergAlternately(word1, word2)
print(result)
