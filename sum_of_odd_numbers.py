'''
Given the triangle of consecutive odd numbers:
           1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
'''
import itertools
def generate_odd():
    i=1
    while True:
        if i%2!=0:
            yield i
        i+=1

def row_sum_odd_numbers(i):
    total_odd_nums_to_generate = int((i*(i+1))/2) #sum([e for e in range(1,i+1)])
    #print(total_odd_nums_to_generate)
    odd_iter = generate_odd()
    s=itertools.islice(odd_iter,total_odd_nums_to_generate-i, total_odd_nums_to_generate)
    return sum(s)

def main():
    i=int(input('Enter the row number: '))
    s=row_sum_odd_numbers(i)
    print(s)    
if __name__=='__main__':
    main()