str = 'racecar'


def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) -1
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex = startIndex + 1
        endIndex = endIndex - 1
    return True

print (isPalindrome("racvcar"))