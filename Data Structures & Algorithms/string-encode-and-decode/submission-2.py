class Solution:

    def encode(self, strs: List[str]) -> str:
        a=''
        for s in strs:
            a+=''.join(s+'é')
        print(a)
        return a

    def decode(self, s: str) -> List[str]:
        l=[]
        a=''
        for i in s:
            if i=='é':
                l.append(a)
                a=''
            else:
                a+=i

        return l
                
                 

