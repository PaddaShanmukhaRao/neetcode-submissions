class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        seq=[]
        if len(nums)==0:
            return 0
        count=1
        maxcount = 1
        for i in nums:
            if i-1 not in temp and i+1 in temp:
                seq.append(i)
        print(seq)
        for i in seq:
            temp1 = i
            while True:
                if temp1+1 in temp:
                    print("Hi")
                    count+=1
                    temp1+=1
                else:
                    print("else block")
                    maxcount = max(maxcount,count)
                    count=1
                    break
        return maxcount