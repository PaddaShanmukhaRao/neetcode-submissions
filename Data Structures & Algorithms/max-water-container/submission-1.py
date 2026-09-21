class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxw=0
        curw=0
        while l<r:
            curw = min(heights[l],heights[r])*(r-l)
            maxw = max(maxw,curw)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            #l+=1
            #r-=1
        return maxw