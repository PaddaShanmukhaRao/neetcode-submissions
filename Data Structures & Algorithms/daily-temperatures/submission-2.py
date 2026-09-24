class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []
        index=[]
        for i in range(len(temperatures)):
            if not st:
                st.append(temperatures[i])
                index.append(i)
            else:
                if temperatures[i]<=st[-1]:
                    st.append(temperatures[i])
                    index.append(i)
                else:
                    while True:
                        if len(st)==0 or temperatures[i]<=st[-1]:
                            st.append(temperatures[i])
                            index.append(i)
                            break
                        else:
                            st.pop()
                            idx = index.pop()
                            res[idx] = i - idx
        return res