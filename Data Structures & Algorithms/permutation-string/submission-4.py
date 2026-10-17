class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)
        ss1 = "".join(sorted(s1))
        while r<=len(s2):
            window = s2[l:r]
            swindow = "".join(sorted(window))
            if swindow==ss1:
                return True
            else:
                l+=1
                r+=1
        return False