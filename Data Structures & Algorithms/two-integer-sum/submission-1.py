class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for cur_index,cur_value in enumerate(nums):
            res = target - cur_value
            if res in d:
                return [d[res],cur_index]
            else:
                d[cur_value]=cur_index
        return False