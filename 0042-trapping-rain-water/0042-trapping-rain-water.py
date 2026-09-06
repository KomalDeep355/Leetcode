class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height [left] > left_max:
                    left_max = height[left]
                else:
                    water_at_left = left_max - height[left]
                    max_water += water_at_left
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_at_right = right_max - height[right]
                    max_water += water_at_right
                right -= 1
        return max_water
             

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna