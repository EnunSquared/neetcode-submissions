class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use set space O(1)
        # check horizontal O(1)
        mem = set()
        for horiz in board:
            mem.clear()
            for j in range(9):
                #print("horiz", mem)
                if horiz[j] != '.' and horiz[j] in mem:
                    return False
                mem.add(horiz[j])
        # check vertical O(1)
        for i in range(9):
            mem.clear()
            for j in range(9):
                #print("vert", mem)
                if board[j][i] != '.' and board[j][i] in mem:
                    return False
                mem.add(board[j][i])

        # check grid
        # loop vertially skip by 3
        for i in range(0, 9, 3):
            # loop horiz skip by 3
            for j in range(0, 9, 3):
                #clear set
                mem.clear()
                # loop 3 horizontal
                for hadd in range(3):
                    # loop 3 vertical
                    for vadd in range(3):
                        print("grid", mem)
                        val = board[i +hadd][j+vadd]
                        # if not '.'
                        # if number in set then return false
                        if val != '.' and val in mem:
                            return False
                        mem.add(board[i+hadd][j+vadd])

        return True
        