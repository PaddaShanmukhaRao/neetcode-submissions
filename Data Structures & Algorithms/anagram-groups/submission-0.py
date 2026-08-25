class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        
        for s in strs:
            c=[0]*26
            for i in s:
                c[ord(i)-ord('a')]+=1
            d[tuple(c)].append(s)
        #print(d)
        return list(d.values())
