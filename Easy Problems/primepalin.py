from math import sqrt

def isprime(test):
	return not any (test % i == 0 for i in range(3, int(sqrt(test)) + 2))
	
for i in range (3, 1000, 2):
	n = str(i)
	if(isprime(i) and n == n[::-1]):
		palindrome = i
print palindrome