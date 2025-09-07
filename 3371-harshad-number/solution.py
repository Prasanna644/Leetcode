class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # Calculate the sum of digits
        digit_sum = sum(int(d) for d in str(x))
        
        # Check if x is divisible by digit_sum (Harshad condition)
        if x % digit_sum == 0:
            print("Harshad Number")
            return digit_sum
        else:
            print("Not Harshad Number")
            return -1
