class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if st:
                if s[i]==')' and st[-1]=='(':
                    st.pop()
                elif s[i]==']' and st[-1]=='[':
                    st.pop()
                elif s[i]=='}' and st[-1]=='{':
                    st.pop()
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
        return len(st)==0
