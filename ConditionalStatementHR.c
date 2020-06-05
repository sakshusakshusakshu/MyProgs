/*
Task
Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
*/
# SOLUTION
#!/bin/python3
if __name__ == '__main__':
    n = int(input())
    if n % 2 == 0 :
        if n >= 2 and n <=5 :
            print("Not Weird")
        if n >= 6 and n <= 20 :
            print("Weird")
        if n > 20 :
            print("Not Weird")
    else :
        print("Weird")
