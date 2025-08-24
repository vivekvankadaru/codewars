'''
Complete the solution so that the function will break up camel casing, using a space between words.
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''

def fetch_pos_of_caps(s):
    pos=[]
    for i in range(len(s)):
        if s[i].isupper():
            pos.append(i)
    return pos
def break_camel_case(s):
    if s==s.lower():
        return s
    else:
        pos_of_caps = fetch_pos_of_caps(s)
        print(pos_of_caps)
        a=''
        p=0
        for i in pos_of_caps:
           if i==len(s)-1:
               a=a+s[p:i]
           else:
                a=a+s[p:i]+' '
           p=i
        a+=s[i:len(s)]
        return a  
def main():
    s=input('Enter string which u want to break camelcase: ')
    s=break_camel_case(s)
    print(s)
if __name__=='__main__':
    main()