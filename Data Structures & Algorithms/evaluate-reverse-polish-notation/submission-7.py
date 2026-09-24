class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        st = []
        res = 0
        op = ['+','-','*','/']
        for i in tokens:
            if i in op:
                op2 = st.pop()
                op1 = st.pop()
                if i == '+':
                    res = op1 + op2
                    st.append(res)
                elif i == '-':
                    res = op1 - op2
                    st.append(res)
                elif i == '*':
                    res = op1 * op2
                    
                    st.append(res)
                elif i == '/':
                    res = int(op1 / op2)
                    st.append(res)
            else:
                st.append(int(i))
        return res