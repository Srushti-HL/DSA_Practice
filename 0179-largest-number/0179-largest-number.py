from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        
        # convert to strings
        nums = list(map(str, nums))
        
        # custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a comes first
            elif a + b < b + a:
                return 1    # b comes first
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        result = "".join(nums)

        # handle leading zeros
        return "0" if result[0] == "0" else result