class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles

        while numBottles >= numExchange:
            i= numBottles // numExchange
            total +=i
            numBottles =i+ (numBottles % numExchange)

        return total