from math import sqrt

def isprime(test):
	return not any (test % i == 0 for i in range(3, int(sqrt(test)) + 2))
	
	
test_num = 3 
sum = 5

prime_count = 2 

while True: 

	test_num += 2 

	if(isprime(test_num)):
		x = test_num
		prime_count += 1
		sum += x
		if prime_count == 1000:
			break
		
print sum
