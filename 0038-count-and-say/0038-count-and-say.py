class Solution:
    def countAndSay(self, n: int) -> str:
        prev_string = "1"

        for i in range(1, n):
            count = 1
            res = ""

            for j in range(1, len(prev_string)):
                if prev_string[j] == prev_string[j - 1]:
                    count += 1
                else:
                    res += str(count) + prev_string[j - 1]
                    count = 1

            res += str(count) + prev_string[-1]
            prev_string = res

        return prev_string

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna