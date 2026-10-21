class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                #means the left side is sorted. then we have to check if the target is in between them or no
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    #the target exists on the right side of the list
                    left = mid + 1
            else:
                #means the right side is sorted. then we have to check if the target is in between mid and right or no
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1