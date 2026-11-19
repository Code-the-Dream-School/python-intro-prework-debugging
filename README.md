# Task 2: Debugging a Short Script

The script calculates the price of a movie ticket. The comments at the top of the script describe what the script should do. The script has four errors:
• Three errors cause Python to show an error message.
• One error does not cause an error message. The script runs, but it gives the wrong result for one of the example runs in Step 3.

## Step 1: Open the script

1.  Open the debugging notebook in Google Colab.
2.  Click File, then Save a copy in Drive. Colab opens your copy in a new tab. Work in your copy, because Colab does not save changes to the original notebook.

## Step 2: Find and fix the errors

Python stops at the first error it finds, so you will see only one error message at a time. Repeat these steps until the script runs without an error message:
1.  Run the script.
2.  Read the error message. The last line names the type of error. The line number shows where Python found the problem. The cause of the problem is sometimes on an earlier line.
3.  Fix the error.
4.  Above the line you changed, add a comment that explains your fix in your own words. Start the comment with # Fix and a number. Example: # Fix 1: I added a missing closing parenthesis.
Change only what you need to fix each error. Do not rewrite the script or add new features.

## Step 3: Test your script

When the script runs without an error message, run it three times with the inputs below. Your output must match these example runs exactly.
```
# Example run 1
# Inputs: Maria, 30
# Output: Hello, Maria
#         Your adult ticket costs 12 dollars.

# Example run 2
# Inputs: Sam, 8
# Output: Hello, Sam
#         Your child ticket costs 8 dollars.

# Example run 3
# Inputs: Lee, 65
# Output: Hello, Lee
#         Your senior ticket costs 8 dollars.
```
If one of your outputs does not match, an error remains. Read the comments at the top of the script again, and compare them with what the code does.

## Step 4: Download your script as a .py file

In Task 3, you will upload your fixed script to GitHub so that we can review it.
1.  In Google Colab, click File, then Download, then Download .py.
2.  Rename the file CTD_prework_debug_yourname.py, and replace yourname with your own name. Example: CTD_prework_debug_maria.py.
3.  Remember where you saved the file. You will need it in Task 3.
Check your work
Before you continue, confirm all of the following:
• Your script runs without an error message.
• Your output matches all three example runs.
• Your script has four # Fix comments, one for each error.
