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


def knap(W, w, v):
    print "Volume limit: " + str(W)
    print "weight: " + str(w)
    print "value: " + str(v)
    # no of items
    nu = len(w)
    opt = [[0 for x in range(W+1)] for x in range(nu+1)]
    for i in range(nu+1):
        for j in range(w[i-1], W+1):
            if i == 0 or j == 0:
                opt[i][j] = 0
                # elif j >= w[i-1]:
                # corresponding value for ith item is in index i-1
                # opt[i][j] = max(opt[i-1][j], opt[i-1][j-w[i-1]]+v[i-1])
                # else:
                # opt[i][j] = opt[i-1][j]
            else:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j-w[i-1]]+v[i-1])
            print opt
    print opt[nu][W]
    return opt[nu][W]


def knap2(W, w, v):
    print "Volume limit: " + str(W)
    print "weight: " + str(w)
    print "value: " + str(v)
    # no of items
    nu = len(w)
    opt = [0 for x in range(W+1)]
    for i in range(nu+1):
        for j in range(W, w[i-1]-1, -1):
            if i == 0 or j == 0:
                opt[j] = 0
            else:
                opt[j] = max(opt[j-1], opt[j-w[i-1]]+v[i-1])
                print opt
    print opt[W]
    return opt[W]


def lcs(s1, s2):
    print s1, s2

    dp = [[0 for x in range(len(s1)+1)] for x in range(len(s2)+1)]

    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            # if i == 0 or j == 0:
            #     dp[i][j] = 0
            # else:
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        print dp

    i = len(s2)
    j = len(s1)
    print dp[i][j]

    size = dp[i][j]
    cs = ["-"]*size

    # print i
    # print j
    while i>0 and j>0 and size > 0:
        if s1[j-1] == s2[i-1]:
            cs[size-1] = s1[j-1]
            size -= 1
            i -= 1
            j -= 1
        else:
            # go to the direction with greater value
            if dp[i][j-1] > dp[i-1][j]:
                j -= 1
            else:
                i -= 1

    print "".join(cs)
    # return dp[i][j]


def lis(s):
    print s

    dp = [1 for x in range(len(s)+1)]

    for i in range(2, len(s)+1):
        for j in range(1, i):
            if s[j-1] < s[i-1]:
                dp[i-1] = max(dp[j-1]+1, dp[i-1])
            else:
                dp[i-1] = max(dp[:i-1])

    print dp




def main(args):
    # reverse_sentence(args[0])
    # find_2nd_largest(args)
    # lcs(args[0], args[1])
    lis(args[0])

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
