class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDuplicates(cells):
            seen = set() 
            for val in cells:
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True

        def getBox(box_row, box_col):
            start_row = box_row * 3
            start_col = box_col * 3
            values = []
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    values.append(board[i][j])
            return values

        for i in range(9):
            row = [board[i][j] for j in range(9)]
            if not hasDuplicates(row):
                return False

        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not hasDuplicates(col):
                return False

        for box_row in range(3):
            for box_col in range(3):
                box = getBox(box_row, box_col)
                if not hasDuplicates(box):
                    return False
        return True


