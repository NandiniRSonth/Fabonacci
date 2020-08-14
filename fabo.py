# Display Fibonacci series up to n-th term

terms = int(input("How many terms? "))

# assigning first two terms of the sequence
n1 = 0
n2 = 1
index = 0

# checking if the number of terms is valid in sequence
if terms <= 0:
   print("Please enter a positive number.")
elif terms == 1:
   print("The Fibonacci sequence upto",terms,":")
   print(n1)
else:
   print("The Fibonacci sequence is:")
   while index < terms:
       print(n1)
       n = n1 + n2
       # update terms
       n1 = n2
       n2 = n
       index += 1