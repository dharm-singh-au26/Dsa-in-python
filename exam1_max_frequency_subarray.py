'''
You are given an array A of integers of size N.
Let X be the frequency of a most frequent number in A.
Return the length of a shortest subarray such that the frequency of its most frequent number is also X.

Input Format

First line of input contains an integer N
Second line contains N space seperated integers A[0], A[1] , A[2] .. A[N-1].
Constraints

N<=100000

Output Format

Print length of the required subarray

Sample Input 0

6
1 2 3 4 3 1
Sample Output 0

3
Explanation 0

The most frequent numbers are 1 and 3 and each of them occur twice, so X = 2. And the sublist [3, 4, 3] is the shortest sublist such that the frequency of the most frequent number is equal to X.

Sample Input 1

10
8 6 9 4 5 4 7 4 2 2 
Sample Output 1

5

'''
def max_freq_array(arr, n):
    left = dict()

    count = dict()
    maxx = 0

    minn, strindex = 0, 0

    for i in range(n):
        x = arr[i]
        if (x not in count.keys()):
            left[x] = i
            count[x] = 1
        else:
            count[x] += 1

        if (count[x] > maxx):
            mx = count[x]
            minn = i - left[x] + 1
            strindex = left[x]
            
        elif (count[x] == maxx and
            i - left[x] + 1 < minn):
            minn = i - left[x] + 1
            strindex = left[x]
    ans = 0
    for i in range(strindex, strindex + minn):
        ans += 1
    return ans
n= int(input())
arr = list(map(int, input().split()))
print(max_freq_array(arr, n))