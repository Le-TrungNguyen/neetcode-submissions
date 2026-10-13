class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                square = (r // 3, c // 3)

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if square not in squares:
                    squares[square] = set()

                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[square]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[square].add(num)

        return True