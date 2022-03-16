'''
You are given a string S of size N.
S contains "1", "2", "3" and "?" only.
you can replace any “?” with "1", "2" or "3".
What is the smallest number you can make as a string such that no two replaced adjacent digits are the same.

Input Format

First and only line of input contains string S
Constraints

N<=100000

Output Format

print the required answer

Sample Input 0

3?2??
Sample Output 0

31212
Sample Input 1

???
Sample Output 1

121
Sample Input 2

111??222??
Sample Output 2
'''

def adjacent(String1,n):
    for i in range(n):
        if String1[i] == "?":
            if i == 0:
                if String1[i + 1] != "1":
                    String1[i] = "1"
                elif String1[i + 1] != "2":
                    String1[i] = "2"
                else:
                    String1[i] = "3"
            elif i == n - 1:
                if String1[i - 1] != "1":
                    String1[i] = "1"
                elif String1[i - 1] != "2":
                    String1[i] = "2"
                else:
                    String1[i] = "3"
            else:
                if String1[i - 1] != "1" and String1[i + 1] != "1":
                    String1[i] = "1"
                elif String1[i - 1] != "2" and String1[i + 1] != "2":
                    String1[i] = "2"
                else:
                    String1[i] = "3"
    print("".join(String1))
str = input()
n1 = len(str)
string1 = list(str)
adjacent(string1,n1)