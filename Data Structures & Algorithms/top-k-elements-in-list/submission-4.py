class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1

        freq=[[] for i in range(len(nums)+1)]
        for num,cnt in c.items():
            freq[cnt].append(num)
        #print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            if len(freq[i]):
                for num in freq[i]:
                    res.append(num)
                    print("res is",res)
                    if len(res)==k:
                        return res

