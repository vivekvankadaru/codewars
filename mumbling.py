'''
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

def accum(st):
    l_st = list(st)
    l1_st = [st[ele].upper()+(st[ele].lower())*(ele) for ele in range(len(st))]
    return '-'.join(l1_st)
def main():
    s = input('Enter the string: ')
    final_s = accum(s)
    print(final_s)
if __name__ == '__main__':
    main()