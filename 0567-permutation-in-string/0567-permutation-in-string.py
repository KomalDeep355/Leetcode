class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = 0
        count_s1 = {}
        count_window = {}

        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        while right < len(s2):
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                count_window[s2[left]] -= 1

                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]

                left += 1

            if count_window == count_s1:
                return True

            right += 1

        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna