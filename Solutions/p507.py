class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum_divisors = 1  
        for j in range(2, int(num**0.5) + 1):
            if num % j == 0:
                sum_divisors += j
                if j != num // j:  
                    sum_divisors += num // j
        return sum_divisors == num

'''
optimized version of basic perfect number code, we are not iterating all elements till nth number but iterating till only root of nth element
'''
