class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        n1  = 0
        flower = flowerbed
        for i in range(len(flower)):

            if (flower[i] == 0) and (i==0 or flower[i-1]==0) and (i == len(flower) -1 or flower[i+1] == 0):

                flower[i] = 1

                counter += 1

                if counter >= n:
                    return True

        return counter >= n
