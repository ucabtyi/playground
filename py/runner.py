import sys


def is_anagrams(a, b):
    pass


def reverse_sentence(s):
    new = ""
    temp = s.split(" ")
    for i in range(len(temp)-1, -1, -1):
        new += "%s " % temp[i]

    print str(new)


def find_2nd_largest(arr):
    fir = sec = None
    for nu in arr:
        nu = int(nu)
        if fir is None:
            fir = nu
            continue
        if fir < nu:
            sec = fir
            fir = nu
            continue
        if sec is None:
            sec = nu
            continue
        if sec < nu < fir:
            sec = nu
            continue

    print sec
    return sec


def main(args):
    # reverse_sentence(args[0])
    find_2nd_largest(args)


if __name__ == "__main__":
    main(sys.argv[1:])



'''
IsAnagram
Count unique substring of length k  
leet code problem
'''

'''
Given two JSON, write a function to find the differences in them  
mplement a BST with the methods `put(t)`, `contains(t)` and `in_order_traversal`.
implement hashmap
'''