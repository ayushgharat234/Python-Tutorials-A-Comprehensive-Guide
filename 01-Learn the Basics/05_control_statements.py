"""
Control Statements in Python:

Control statements are used to control the flow of execution in Python.
- `if`, `elif`, `else`: Conditional statements
- `break`, `continue`: Loop control
"""

# Example 1: If-Else Statements
num = 10
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Explanation:
# The `if` statement checks if the number is greater than 0. If true, it prints "The number is positive."
# The `elif` (else if) is used if the `if` condition is false, to check another condition (whether the number is zero).
# The `else` block runs when all previous conditions are false, which is when the number is negative.

# Example 2: Using 'break' in a loop
for i in range(5):
    if i == 3:
        break  # Exits the loop when i equals 3
    print(i)

# Explanation:
# The loop iterates through numbers from 0 to 4. When `i` equals 3, the `break` statement terminates the loop immediately.
# This results in the output "0, 1, 2", and the loop stops without printing 3 or 4.

# Example 3: Using 'continue' in a loop
for i in range(5):
    if i == 2:
        continue  # Skips the current iteration when i equals 2
    print(i)

# Explanation:
# The loop iterates through numbers from 0 to 4. When `i` equals 2, the `continue` statement skips the current iteration.
# This means 2 is not printed, and the loop continues with 3, 4. The output will be "0, 1, 3, 4".

"""
Key Concepts:

1. **If-Else Statements**:
   - Conditional statements used to check whether a condition is true or false.
   - `if` runs if the condition is true.
   - `elif` (optional) allows multiple conditions to be checked.
   - `else` runs when none of the previous conditions are true.

2. **Break Statement**:
   - Exits the loop immediately, regardless of whether the loop condition has been met.
   - Useful for stopping the loop early when a certain condition is satisfied.

3. **Continue Statement**:
   - Skips the current iteration of the loop and moves to the next iteration.
   - Used when you want to skip specific cases or conditions without breaking out of the loop completely.

"""