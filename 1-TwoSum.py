class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        nums_sorted = sorted(enumerate(nums), key= lambda x: x[1])
        print(nums_sorted)
        while left < right:
            total =  nums_sorted[left][1] + nums_sorted[right][1]
            if total == target:
                return [nums_sorted[left][0], nums_sorted[right][0]]
            elif total < target:
                left +=1
            else:
                right-=1