string = " "
for i in range (1,100):
	if i%3 ==0:
		string=string+"Fizz" #Multiple of 3#
		continue
	if i%5 ==0:
		string=string+"Buzz"# Multiple of 5#
		continue
	if i%15 ==0:
		string=string+"Fizzbuzz" # multiple of 15#
print(string)
