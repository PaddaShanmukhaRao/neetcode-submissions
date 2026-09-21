class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        prefix=[0]*len(height)
        prefix[0]=height[0]
        suffix=[0]*len(height)
        suffix[-1] = height[-1]
        for i in range(1,len(height)):
            if height[i]>prefix[i-1]:
                prefix[i]=height[i]
            else:
                prefix[i]=prefix[i-1]
        #print(prefix)
        for i in range(len(height)-2,-1,-1):
            if height[i]<suffix[i+1]:
                suffix[i]=suffix[i+1]
            else:
                suffix[i]=height[i]
        #print(suffix)
        for i in range(1,len(height)-1):
            res+= min(prefix[i],suffix[i])-height[i]
        return res