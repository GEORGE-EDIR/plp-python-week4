count = 1
total = 0

# BUG: The while statement was missing a colon (:).
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The loop originally used count < 5, which stopped at 4.
# Changed it to count <= 5 so that 5 is included in the sum.

# BUG: The total is an integer, so it cannot be joined directly to a string.
# Converted total to a string using str().
print("Sum of 1 to 5 is: " + str(total))

