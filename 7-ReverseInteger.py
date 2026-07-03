class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)
        reversed_number = ""
        if number[0] == "-":
            end = 0
        else:
            end = -1
        for i in range(len(number)-1, end, -1):
            reversed_number += number[i]
        if end == 0:
            reversed_number = int(reversed_number)*-1
        else:
            reversed_number = int(reversed_number)
        if reversed_number >= pow(2,31) or reversed_number < -pow(2,31):
            return 0
        return reversed_number