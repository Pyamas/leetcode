class Soultion:
    def candie(self, candies, extraCandies):
        max_candies = max(candies)
        result = []
        for i in candies:
            total_candies = i + extraCandies
            result.append(total_candies >= max_candies)
        return result
                

candies = [2,3,5,1,3]
extraCandies = 3

rozwiazanie = Soultion()
result = rozwiazanie.candie(candies, extraCandies)
print(result)