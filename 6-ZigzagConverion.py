#Complexity O(N)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        new_s = []
        curr_row = 0
        i = 0
        length = len(s)
        direction = 1
        if numRows == 1:
            return s
        while curr_row < numRows and i < len(s):
            new_s.append(s[i])
            if direction == 1:
                i += 2*(numRows-curr_row-1)
            else:
                i+=2*(curr_row)
            if curr_row != 0 and curr_row != numRows-1:
                direction = direction*-1
            if i >= len(s):
                curr_row+=1
                if curr_row == numRows-1:
                    direction = -1
                else:
                    direction = 1
                i=curr_row

        return ''.join(new_s)