def isPalindrome(int x)
{
        s = str(x)
        i = 0
        j = len(s)-1
        r = True
        while i < j:
            if s[i] != s[j]:
                r = False
                break
            i += 1
            j -= 1
        return r
}
