class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        operators = { '+' , '-', '*','/'}
        for token in tokens:
            if token in operators:

                b = st.pop()
                a = st.pop()

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)

                st.append(res)

            else:
                st.append(int(token))

        return st[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna