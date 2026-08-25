class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1

        arr=[]
        for num,cnt in c.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)
        res=[]
        for i in range(k):
            res.append(arr[i][1])
        return res
