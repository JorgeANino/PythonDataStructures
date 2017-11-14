def is_balanced(root):
    ret, h = is_balanced_helper(root)
    return ret

def is_balanced_helper(root):
    if not root:
        return True, 0
    else:
        retl, hl = is_balanced_helper(root.left)
        retr, hr = is_balanced_helper(root.right)
        h = max(hr, hl)+1
        if retl and retr:
            return abs(hl-hr) < 2, h
        else:
            return False, h