    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i = 0 # index of rows
        d = 1 #direction if 1 to down if -1 go up
        rows = [[] for _ in range(numRows)] # Create a matrix with numRows
        for char in s:
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows -1:
                d = -1

            # if it not the first or last index then its the center
            i += d

        ret = ''
        for i in range(numRows):
            ret += ''.join(rows[i])

        return ret

convert("PAYPALISHIRING", 3)

#Expected output Output: "PAHNAPLSIIGYIR"
'''P   A   H   N
A P L S I I G
Y   I   R'''