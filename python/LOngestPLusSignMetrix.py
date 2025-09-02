

class Solution:
    """
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.


"""
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for (x, y) in mines:
            grid[x][y] = 0

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        # FIll left and right
        for r in range(n):
            count = 0
            for c in range(n):
                count = count + 1 if grid[r][c] == 1 else 0
                left[r][c] = count
            count = 0
            for c in range(n-1, -1, -1):
                count = count + 1 if grid[r][c] == 1 else 0
                right[r][c] = count

        #fill up and down
        for c in range(n):
            count = 0
            for r in range(n):
                count = count + 1 if grid[r][c] == 1 else 0
                up[r][c] = count
            count = 0
            for r in range(n-1,-1, -1):
                count = count + 1 if grid[r][c] == 1 else 0
                down[r][c] = count
        
        ans = 0
        for r in range(n):
            for c in range(n):
                order = min(left[r][c], right[r][c], up[r][c], down[r][c])
                print(f"order is {order} in location {r, c}")
                ans = max(ans, order)
        return ans



"""
A farmer wants to farm their land with the maximum area where good land is present. The land represented as a matrix with 1 and 0
where 1 mean "good land" and 0s mean bad land. The farmer only wants to farm in a square of good land with the maximum area. PLease help the farmer to find the maximum
area of the land they can farm in good land
"""


def maximumSquare(matrix: list[list[str]])->int:
    if not matrix or not matrix[0]:
        return 0
    max_sqaure = 1
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]* (cols + 1)  for _ in range(rows + 1)]
    
    
    for r in range(rows):
        for c in range(cols):
            
            if matrix[r][c] == "1":
                top = dp[r][c+1]
                left = dp[r+1][c]
                diag = dp[r][c]
                print(f"row {r} col {c} dp[r][c+1] {dp[r][c+1]} dp[r+1][c] {dp[r+1][c]} dp[r][c] {dp[r][c]}")
                dp[r+1][c+1] = 1 + min(top, left, diag)
                
                max_sqaure = max(max_sqaure, dp[r+1][c+1])
    for i in range(len(dp)):
        print(f"{dp[i]}")
    print(f"max_sqaure {max_sqaure}")
    return max_sqaure

matrix1 = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

# Result = 2

maximumSquare(matrix1)


Got it — Workplace Starter for info@prismmedia.co.ke. Here are the settings to use in Gmail, other mail clients, and on your website.

Use this for incoming:

IMAP (recommended): Host: workplace.truehost.cloud, Port: 993, Encryption: SSL/TLS, Username: info@prismmedia.co.ke, Password: your mailbox password
POP3 (if you must): Host: workplace.truehost.cloud, Port: 995, Encryption: SSL/TLS, Username: info@prismmedia.co.ke, Password: your mailbox password
Use this for outgoing (send email from Gmail or your site):

SMTP: Host: workplace.truehost.cloud, Port: 587 (TLS) or 465 (SSL), Encryption: STARTTLS/TLS (use 465 for SSL), Authentication required: Yes, Username: info@prismmedia.co.ke, Password: your mailbox password
SMTP auth is required for sending from other providers or your website.
Notes you must know:

Always use the full email as the username.
If adding to Gmail, choose to add another email account and supply the SMTP details above; Gmail will ask to verify by sending a code to the mailbox.
For WordPress or other website apps, use an SMTP plugin (WP Mail SMTP, Easy WP SMTP, or similar) and enter the SMTP host, port, TLS/SSL option, username and password. Set From address to info@prismmedia.co.ke and enable authentication.
If your website is hosted on Truehost shared hosting, use SMTP (587/TLS) rather than PHP mail() — PHP mail is disabled on shared hosting.
Do you want step-by-step instructions to add this account into Gmail or a WordPress site now?