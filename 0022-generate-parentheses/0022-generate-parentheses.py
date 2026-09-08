class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(st))
                return

            if open < n:
                st.append("(")
                backtrack(open + 1, closed)
                st.pop()

            if closed < open:
                st.append(")")
                backtrack(open, closed + 1)
                st.pop()

        backtrack(0, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna