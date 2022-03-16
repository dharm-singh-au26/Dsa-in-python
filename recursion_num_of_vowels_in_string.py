"""
Question 1. Write a program using recursion to count the number of
vowels in a string.
"""


def isVowel(ch):
	return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def countVovels(str, n):
	if (n == 1):
		return isVowel(str[n - 1]);

	return (countVovels(str, n - 1) +
				isVowel(str[n - 1]));

str = "hey";


print(countVovels(str, len(str)))

