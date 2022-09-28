# -*- coding: utf-8 -*-
"""
Charles Truscott Watters
Exhaustive Enumeration, Branch and Bound and Greedy Implementations of the first 10 divisors of one
runfile('C:/Users/Visual_Studio/Desktop/CHARLESTRUSCOTTWATTERSALG.py', wdir='C:/Users/Visual_Studio/Desktop')
1 / 1 is 1.0
1 / 2 is 0.5
1 / 3 is 0.3333
1 / 4 is 0.25
1 / 5 is 0.2
1 / 6 is 0.1667
1 / 7 is 0.1429
1 / 8 is 0.125
1 / 9 is 0.1111
[0.9999999999999062, 0.49999999999996125, 0.3332999999999796, 0.2499999999999888, 0.1999999999999943, 0.16669999999999796, 0.14290000000000058, 0.12500000000000255, 0.11110000000000216, 0.10000000000000184]

runfile('C:/Users/Visual_Studio/Desktop/CHARLESTRUSCOTTWATTERSALG.py', wdir='C:/Users/Visual_Studio/Desktop')
1 / 1 is 1.0
1 / 2 is 0.5
1 / 3 is 0.3333
1 / 4 is 0.25
1 / 5 is 0.2
1 / 6 is 0.1667
1 / 7 is 0.1429
1 / 8 is 0.125
1 / 9 is 0.1111
0.9999999999999062 is the divisor of	1 over 	1
0.49999999999996125 is the divisor of	1 over 	2
0.3332999999999796 is the divisor of	1 over 	3
0.2499999999999888 is the divisor of	1 over 	4
0.1999999999999943 is the divisor of	1 over 	5
0.16669999999999796 is the divisor of	1 over 	6
0.14290000000000058 is the divisor of	1 over 	7
0.12500000000000255 is the divisor of	1 over 	8
0.11110000000000216 is the divisor of	1 over 	9
0.10000000000000184 is the divisor of	1 over 	10

Thank you edX

I love you Dad Mark William Watters 1955 until forever

Love my Algorithms and Data Structures, thank you MIT for allowing me into your course and also Kulikov, Pevzner et alia and Compeau et alia

"""


def first_ten_divisors_of_one_exhaustive_and_b_and_b(a = 1, b = list(x for x in range(1, 1 + 10, 1))):
    epsilon = 0.0001
    for x in range(1, b[9], 1):
        while(round((a / b[x - 1]), 4) != round(epsilon, 4)):
            epsilon += 0.0001
#            print("Trying {} for {} over {}".format(epsilon, a, b))
        print("{} / {} is {}".format(a, b[x - 1], round(epsilon, 4)))
        epsilon = 0

def first_ten_divisors_of_one_greedy(a = 1, b = list(x for x in range(1, 1 + 10, 1))):
    R = []
    for x in b:
        maximum = x
        minimum = (maximum / maximum) / 10000
        L = []
        while round(minimum, 4) != round(1 / x, 4):
            minimum += 0.0001
            L.append(minimum)
        R.append(minimum)
    for divisor in b:
        for minum in R:
            if round(minum, 4) == round(1 / divisor, 4):
                print("{} is the divisor of\t{} over \t{}".format(minum, 1, divisor))
        
def main():
    first_ten_divisors_of_one_exhaustive_and_b_and_b()
    first_ten_divisors_of_one_greedy()
    
if __name__ == "__main__": main()