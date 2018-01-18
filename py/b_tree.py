import sys

class Node:

    def __init__(self, value, l=None, r=None):
        self.value = value
        self.l = l
        self.r = r

    def __str__(self):
        s = "value: " + str(self.value)
        if self.l:
            s += " L: %s" % str(self.l.value)
        else:
            s += " L: None"
        if self.r:
            s += " R: %s" % str(self.r.value)
        else:
            s += " R: None"
        # return str(self.value)
        return s


class BTree:

    def __init__(self):
        self.root = None

    def __repr__(self):
        def _repr(node):
            if node:
                print str(node)
                print "goto L"
                _repr(node.l)
                print "search result: %s" % str(node)
                print "goto R"
                _repr(node.r)

        if self.root:
            _repr(self.root)
        else:
            print None


    def _left(self, node_value, new_value):
        return new_value < node_value

    def _right(self, node_value, new_value):
        return new_value > node_value

    def add_v(self, value):
        def _add_v(node, value):
            if value == node.value:
                print "equals..."
                return
            elif self._left(node.value, value):
                if node.l:
                    _add_v(node.l, value)
                else:
                    node.l = Node(value)
            else:
                if node.r:
                    _add_v(node.r, value)
                else:
                    node.r = Node(value)

        if self.root is None:
            self.root = Node(value)
        else:
            _add_v(self.root, value)

    def find_v(self, value):
        def _find_v(node, value):
            if value == node.value:
                print "found..."
                return node
            elif self._left(node.value, value):
                if node.l:
                    _find_v(node.l, value)
                else:
                    print "not found..."
                    return None
            else:
                if node.r:
                    _find_v(node.r, value)
                else:
                    print "not found..."
                    return None

        if self.root:
            _find_v(self.root, value)
        else:
            print "not found..."
            return None

    def print_t(self):
        thislevel = [self.root]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print n.value,
                if n.l: nextlevel.append(n.l)
                if n.r: nextlevel.append(n.r)
            print
            thislevel = nextlevel

    def revert(self):
        def _revert(node):
            if node:
                node.l, node.r = _revert(node.r), _revert(node.l)
            return node

        if self.root:
            _revert(self.root)


    def max_sum_l2l(self):
        def max_sum_path(node, opt):
            if node is None:
                return 0

            l_sum = max_sum_path(node.l, opt)
            r_sum = max_sum_path(node.r, opt)

            if node.l and node.r:
                # important -- result only valid for a node contains both children
                # otherwise no leaf to leaf
                opt[0] = max(opt[0], l_sum+r_sum+node.value)
                print "current max: " + str(opt)
                return max(l_sum, r_sum) + node.value

            return node.value + l_sum + r_sum

        opt = [-sys.maxint-1]
        max_sum_path(self.root, opt)
        print "result: " + str(opt)

    def max_sum_n2n(self):
        def max_sum_path(node, opt):
            if node is None:
                return 0

            l_sum = max_sum_path(node.l, opt)
            r_sum = max_sum_path(node.r, opt)

            # 4 situations -- node only, node + left max, node + right max, node + both max(go through)
            opt[0] = max(opt[0], node.value, node.value+l_sum, node.value+r_sum, node.value+l_sum+r_sum)

            if node.l and node.r:
                # max path sum -- can only count one side
                return max(max(l_sum, r_sum) + node.value, node.value)

            else:
                return max(node.value + l_sum + r_sum, node.value)

        opt = [-sys.maxint-1]
        max_sum_path(self.root, opt)
        print "result: " + str(opt)



def main(args):
    tree = BTree()
    # tree.add_v(5)
    # tree.add_v(9)
    # tree.add_v(6)
    # tree.add_v(7)
    # tree.add_v(4)
    # tree.add_v(3)
    # tree.add_v(1)
    # tree.add_v(8)
    # tree.add_v(11)
    # tree.add_v(10)
    tree.root = Node(10)

    tree.root.l = Node(-1)
    tree.root.r = Node(-2)

    # tree.root.l = Node(5)
    # tree.root.r = Node(6)
    # tree.root.l.l = Node(-8)
    # tree.root.l.r = Node(1)
    # tree.root.l.l.l = Node(2)
    # tree.root.l.l.r = Node(6)
    # tree.root.r.l = Node(3)
    # tree.root.r.r = Node(9)
    # tree.root.r.r.r= Node(0)
    # tree.root.r.r.r.l = Node(4)
    # tree.root.r.r.r.r = Node(-1)
    # tree.root.r.r.r.r.l = Node(10)

    # tree.root.l = Node(2)
    # tree.root.r   = Node(10);
    # tree.root.l.l  = Node(20);
    # tree.root.l.r = Node(1);
    # tree.root.r.r = Node(-25);
    # tree.root.r.r.l   = Node(3);
    # tree.root.r.r.r  = Node(4);

    # print tree.root
    # print str(tree.__repr__())
    tree.print_t()
    # tree.revert()
    print "#####"
    # tree.print_t()
    # tree.find_v(111)
    # tree.max_sum_l2l()
    tree.max_sum_n2n()


if __name__ == "__main__":
    main(sys.argv[1:])
