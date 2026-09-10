class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0

        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] == "+":
            i += 1

        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        while i < len(s):
            if s[i] == "0":
                result = result * 10
            elif s[i] >= "1" and s[i] <= "9":
                result = result * 10 + int(s[i])
            else:
                break

            i += 1

        result *= sign

        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1

        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna