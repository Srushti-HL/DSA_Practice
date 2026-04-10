class Solution:
    def reverseBits(self, n):
        result = 0
        
        for _ in range(32):
            bit = n & 1          # get last bit
            result = (result << 1) | bit
            n >>= 1             # shift right
        
        return result