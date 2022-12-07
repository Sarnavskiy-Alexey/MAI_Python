"""
    Reference: https://www.codewars.com//kata/5e320fe3358578001e04ad55
    Decision can be verified after some test executions because it doesn't care about other figures in one line between figure and King
"""


is_check=lambda b:sum([b[k][n]=='♟'and i-k==abs(j-n)==1or b[k][n]in'♝♛'and abs(i-k)==abs(j-n)or b[k][n]in'♜♛'and(i==k or j==n)or b[k][n]=='♞'and abs(i-k)+abs(j-n)==3and abs(j-n)in(1,2)for k in range(8)for n in range(8)for i in range(8)for j in range(8)if b[i][j]=='♔'])>0
