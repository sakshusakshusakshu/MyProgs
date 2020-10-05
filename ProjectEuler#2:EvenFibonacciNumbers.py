"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with  and , the first  terms will be:

By considering the terms in the Fibonacci sequence whose values do not exceed , find the sum of the even-valued terms.

Input Format

First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .

Constraints

Output Format

Print the required answer for each test case.

Sample Input 0

2
10
100
Sample Output 0

10
44
Explanation 0

For , we have , sum is .
For , we have , sum is .
"""
# SOLUTION
#!/bin/python3

import sys
def evenFibbSum(n):
    if n < 2 :
        return 0
    evenFibb1 = 0
    evenFibb2 = 2
    Sum = evenFibb1 + evenFibb2

    while evenFibb2 <= n :
        evenFibb3 = 4 * evenFibb2 + evenFibb1

        if evenFibb3 > n :
            break;

        evenFibb1 = evenFibb2
        evenFibb2 = evenFibb3
        Sum += evenFibb2
    return Sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = evenFibbSum(n)
    print(ans)