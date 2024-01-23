class Solution:
    def searchRange(self, nums, target):
        lower_bound = self.findLowerBound(nums, target)
        if (lower_bound == -1):
            return [-1, -1]
        upper_bound = self.findUpperBound(nums, target)
        return [lower_bound, upper_bound]

    def findLowerBound(self, nums, target):
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                if mid == left or nums[mid - 1] < target:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    def findUpperBound(self, nums, target):

        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                if mid == right or nums[mid + 1] > target:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


sol = Solution()
n = sol.searchRange([1, 2, 2, 2, 3, 4, 5], 2)
print(n)
