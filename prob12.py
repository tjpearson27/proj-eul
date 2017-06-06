#find first triangle number with 500 divisors
#create list of triangle numbers
#divide triangle numbers by all number, check for mod 0
#for all mod 0, append number to list
#if len(list) < 500, start over, look at next triangle number

#define method to evaluate each triangle number as it is generated
def nr_divisors(num):
    divisors = []
    half = num/2
    d = 1
    while d <= half:
        if num % d == 0:
            divisors.append(d)
        d += 1
    divisors.append(num)
    l = len(divisors)
    #print divisors
    return l


#generate triangle numbers list
import itertools

last_tri = 1
for n in itertools.count(2):
    tri_num = last_tri + n
    div = nr_divisors(tri_num)
    print div
    last_tri = tri_num
    if div >= 498:
        break
    print tri_num
