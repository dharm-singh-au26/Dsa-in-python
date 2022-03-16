'''
Given a string S of size N.
Print the minimum number of characters that we need to delete to make frequency of each character unique.

Input Format

First and only line of input contains a string S
Constraints

N<=100000

Output Format

Print the required answer

Sample Input 0

aabb
Sample Output 0

1
Explanation 0

Both "a" and "b" occur twice, so we can remove say "a" once to make the frequencies unique.

Sample Input 1

abbccc
Sample Output 1

0
Explanation 1

The string already has unique frequencies for "a", "b" and "c": [1, 2, 3].
'''
def minDeletions(s):
        cnt=0
        idx=[]
        for i in set(s):
            idx.append(s.count(i))
        for i in range(len(idx)):
            ele=idx.pop(0)
            while ele in idx:
                cnt+=1
                ele-=1
            if ele!=0:
                idx.append(ele)
        return cnt
s = "abbccc"
print(minDeletions(s))