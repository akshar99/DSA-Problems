class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        out = []
        for candy in candies:

            if candy + extraCandies >= max_candy:
                out.append(True)

            else:
                out.append(False)

        return out