def isPalindrome(string):
    # Write your code here.
    s = ''
    for i in range(len(string)-1, 0, -1):
        s = s + string[i]
    s = s + string[0]
    print(s)


isPalindrome('abcdcba')
