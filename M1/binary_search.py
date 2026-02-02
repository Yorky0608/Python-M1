class Solution:
    def binarysearch(self, arr, k):
        
        lo, hi = 0, len(arr) - 1
        res = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == k:
                res = mid
                hi = mid - 1  # keep searching left for first occurrence
            elif arr[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return res


test = Solution()
print(test.binarysearch([1, 2, 2, 2, 3, 4, 5], 1))  # Output: 1