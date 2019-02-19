def swap_case(s):
    new = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                new = new + i.lower()
            if i.islower():
                new = new + i.upper()
        else: 
            new = new + i
    return(new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)