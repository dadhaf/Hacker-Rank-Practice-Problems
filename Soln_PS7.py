def swap_case(s):
    a=[]
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                a.append(s[i].lower())
            else:
                a.append(s[i].upper())
        else:
            a.append(s[i])
    return "".join(a)
    
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
 
