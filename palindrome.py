def is_palindrome(text):
  """
  Checks if a given string is a palindrome.

  Args:
    text: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Convert the string to lowercase and remove spaces for case-insensitive and space-agnostic checking
  processed_text = "".join(char.lower() for char in text if char.isalnum())
  
  # Compare the processed string with its reverse
  return processed_text == processed_text[::-1]

# Get input from the user
user_input = input("Enter a string: ")

# Check if it's a palindrome and print the result
if is_palindrome(user_input):
  print(f"'{user_input}' is a palindrome.")
else:
  print(f"'{user_input}' is not a palindrome.")
