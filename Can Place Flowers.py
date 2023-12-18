class Solution(): 
    def plots(self, flowerbed, n):
        maxx = len(flowerbed)
        i = 0 
        while i < maxx: 
            if flowerbed[i] == 1:
                i += 2
            elif i + 1 < maxx and flowerbed[i+1] == 0:
                n-= 1
                i+=2
            else:
                i += 1
        return n <= 0



rozwiazanie = Solution()
flowerbed = [1, 0, 0, 0, 1]
result = rozwiazanie.plots(flowerbed, 1)
print(result)

    