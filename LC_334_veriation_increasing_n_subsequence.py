from typing import List
import bisect

class Solution:
    def increasingSubsequence(self, nums: List[int], k: int) -> bool:
        # Initialize a list to track the smallest subsequence of length k
        subsequence = [float('inf')] * k

        for num in nums:
            # Find the position to insert the current number in the subsequence
            pos = bisect.bisect_left(subsequence, num)
            
            # If the position is less than k, replace the element at pos with num
            if pos < k:
                subsequence[pos] = num
            
            # Check if we have successfully formed a subsequence of length k
            if subsequence[k-1] < float('inf'):
                return True

        return False

nums = [20, 100, 10, 12, 5, 13]
solution = Solution()
k = 3
output = solution.increasingSubsequence(nums, k)
print(output)