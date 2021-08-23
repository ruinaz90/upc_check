import pyinputplus as pyip

upc_input = pyip.inputNum("Enter UPC: ")
upc_number = [int(num) for num in str(upc_input)]   # Convert int input to list

upc_odd = upc_number[:10:2]   # digits in odd position
upc_even = upc_number[1:9:2] # digits in even position
sum_odd = 0
sum_even = 0

# Add digits in odd position and multiply result by 3
for digit in upc_odd:
    sum_odd += digit
sum_odd *= 3

# Add digits in even position
for digit in upc_even:
    sum_even += digit

sum = sum_odd + sum_even

print(upc_number[10])