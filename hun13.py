def rev1(s): 
    return s[::-1] 
def isPalindrome(s): 
    rev = rev1(s)  
    if (s == rev): 
        return True
    return False
s = input()
ans = isPalindrome(s) 
if ans == 1: 
    print("YES") 
else: 
    print("NO") 
