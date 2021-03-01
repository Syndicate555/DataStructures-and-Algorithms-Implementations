def isPalindrome(string):
    # Write your code here.
    s = ''
    for i in range(len(string)-1, -1, -1):
        s = s + string[i]

    return s == string


print(isPalindrome('abcdcba'))
