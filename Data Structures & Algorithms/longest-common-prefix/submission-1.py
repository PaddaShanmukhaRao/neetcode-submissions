class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        if len(strs)==1:
            return strs[0]
        minStr = len(min(strs))
        for i in range(minStr):
            flag=1
            for j in range(len(strs)-1):
                print(j,i)
                if strs[j][i]!=strs[j+1][i]:
                    flag=0
                    return res
            if flag:
                res+=strs[j][i]
        return res
