class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            counter = Counter(
                value for value in board[i] if value != '.'
            )

            if any(count > 1 for count in counter.values()):
                return False

        # Check columns
        for j in range(9):
            counter = Counter(
                board[i][j] for i in range(9)
                if board[i][j] != '.'
            )

            if any(count > 1 for count in counter.values()):
                return False

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values = []

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != '.':
                            values.append(board[i][j])

                counter = Counter(values)

                if any(count > 1 for count in counter.values()):
                    return False

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna