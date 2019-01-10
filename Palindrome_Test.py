# File: Palindrome_Test.py
# Description: A program that tests whether a given string is a palindrome. Runs continually until user enters an empty string.

def isPalindrome(str):
    for i in range(0, len((str)) // 2):
        if str[i] != str[len(str) - i - 1]:
            return False
        else:
            return True

def main():
    inString = input("Enter a string: ").strip()
    print(inString)
    while inString != "":
        if isPalindrome(inString):
            print("'" + inString + "'" + " is a palindrome")
        else:
            print("'" + inString + "'" + " is not a palindrome")
        inString = input("Enter another string: ")
        
main()