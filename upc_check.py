while True:
    upc_input = input("Enter UPC: ")

    # End loop if 11 or 12 digit number
    if upc_input.isnumeric() and 10 < len(upc_input) < 13:
        break
    else:
        print("Please enter an 11 or 12 digit number.")

# Convert int input to list
upc_number = [int(num) for num in upc_input]

upc_odd = upc_number[::2]   # digits in odd position
upc_even = upc_number[1::2] # digits in even position
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

check_digit = 10 - sum % 10

print(f"Check digit is {check_digit}")