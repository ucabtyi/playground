import sys


def merge_sort(arr):
    def _merge_sort(a1, a2):
        print "merging: %s | %s" % (str(a1), str(a2))
        result = []
        i = 0
        j = 0
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                result.append(a1[i])
                i += 1
                if i == len(a1):
                    result.extend(a2[j:])
                    break
            else:
                result.append(a2[j])
                j += 1
                if j == len(a2):
                    result.extend(a1[i:])
                    break
            print result

        print str(result)
        return result

    if len(arr) <= 1:
        print "returning... %s" % str(arr)
        return arr

    print "dealing with ... %s" % str(arr)
    size = len(arr)
    lf = arr[0:size/2]
    rf = arr[size/2:]
    lf = merge_sort(lf)
    rf = merge_sort(rf)

    return _merge_sort(lf, rf)


def main(args):
    merge_sort([4,5,9,8,2,210,5,2])


if __name__ == "__main__":
    main(sys.argv[1:])
