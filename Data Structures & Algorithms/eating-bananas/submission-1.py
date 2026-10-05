class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min_hours >= num piles
        # number of hours/pile = ceil(piles[i] / k)
        # find how long it would take to eat piles with eating rate of k
        # s
        # find upper and lower bound
        # upper = max number in pile
        # lower = 1
        def canEat(self, rate: int) -> bool:
            sum = 0
            for pile in piles:
                sum += math.ceil(pile / rate)
            return sum <= h
        
        upper = max(piles)
        lower = 1
        minimum = upper
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            if canEat(self, mid):
                minimum = min(minimum, mid)
                upper = mid - 1
            else:
                lower = mid + 1
        return minimum

        