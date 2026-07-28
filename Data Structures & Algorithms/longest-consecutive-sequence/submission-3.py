class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet= set(nums)
        if len(nums)==0:
            return 0
        max_seq=1
        for i in numsSet:
            seq=1
            if i-1 not in numsSet:
                while i+1 in numsSet:
                    seq+=1
                    i+=1
                max_seq= max(seq,max_seq)
        return max_seq



