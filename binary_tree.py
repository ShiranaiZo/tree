"""
    https://github.com/QunAlfadrian
    Kyun~#7250

    Todo:
    1. post order list
    2. in order list
    3. level list
"""
# ==============================================================================
class PohonBiner():
    def __init__(self, root:int=None, left:int=None, right:int=None) -> None:
        self.root = root
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return ("(%s, %s, %s)" % (
            repr(self.root), 
            repr(self.left), 
            repr(self.right),
            ))
# ==============================================================================
# Selektor
def akar(P):
    return P.root

def left(P):
    return P.left

def right(P):
    return P.right
# ==============================================================================
# Konstruktor
def makePB(root:int=None, left:int=None, right:int=None):
    """Create Non-Empty Binary Tree

    Parameters
    ----------
    root : int, optional
        Root of Binary Tree, by default None
    left : int, optional
        Left Branch of Binary Tree, by default None
    right : int, optional
        Right Branch of Binary Tree, by default None

    Returns
    -------
    PohonBiner
        Binary Tree
    """
    return PohonBiner(root, left, right)
# ==============================================================================
# Predikat
def is_tree_empty(P:PohonBiner):
    # if (akar(P) == None) and (left(P) == None) and (right(P) == None):
    # if (not akar(P)) and (not left(P)) and (not right(P)):
    #     return True
    # else:
    #     return False
    return P == None

def is_one_elmt(P:PohonBiner):
    if akar(P) and (not left(P)) and (not right(P)):
        return True
    else:
        return False

def is_uner_left(P:PohonBiner):
    if (
        (not is_tree_empty(P) and not is_tree_empty(left(P)))
        and is_tree_empty(right(P))
    ):
        return True
    else:
        return False

def is_uner_right(P:PohonBiner):
    if (
        (not is_tree_empty(P) and not is_tree_empty(right(P)))
        and is_tree_empty(left(P))
    ):
        return True
    else:
        return False

def is_biner(P:PohonBiner):
    if (
        not is_tree_empty(P)
        and not is_tree_empty(left(P))
        and not is_tree_empty(right(P))
    ):
        return True
    else:
        return False
# ==============================================================================
# Fungsi Dasar
def nb_elmt(P:PohonBiner):
    if is_one_elmt(P):
        return 1
    else:
        if is_biner(P):
            return 1 + nb_elmt(left(P)) + nb_elmt(right(P))
        elif is_uner_left(P):
            return 1 + nb_elmt(left(P))
        elif is_uner_right(P):
            return 1 + nb_elmt(right(P))

def nb_daun(P:PohonBiner):
    if is_one_elmt(P):
        return 1
    else:
        if is_biner(P):
            return nb_daun(left(P)) + nb_daun(right(P))
        elif is_uner_left(P):
            return nb_daun(left(P))
        elif is_uner_right(P):
            return nb_daun(right(P))

def rep_prefix(P:PohonBiner):
    """Representate Tree

    Parameters
    ----------
    P : <class 'PohonBiner'>
        Binary Tree

    Returns
    -------
    list
        List of Binary Tree in Prefix format: [root, left, right]
    """
    if is_one_elmt(P):
        return [akar(P)]
    else:
        if is_biner(P):
            return [akar(P)] + [rep_prefix(left(P))] + [rep_prefix(right(P))]
        elif is_uner_left(P):
            return [akar(P)] + [rep_prefix(left(P))] + []
        elif is_uner_right(P):
            return [akar(P)] + [] + rep_prefix(right(P))

def is_exist_left(P:PohonBiner):
    # Kiri ada sub pohon biner
    return (not is_tree_empty(P) and not is_tree_empty(left(P)))

def is_exist_right(P:PohonBiner):
    return (not is_tree_empty(P) and not is_tree_empty(right(P)))
# ==============================================================================
# Predikat Lain
def is_member(P:PohonBiner, X:int):
    if is_tree_empty(P):
        return False
    else:
        if akar(P) == X:
            return True
        else:
            if is_biner(P):
                return is_member(left(P), X) or is_member(right(P), X)
            elif is_uner_left(P):
                return is_member(left(P), X)
            elif is_uner_right(P):
                return is_member(right(P), X)
            else:
                return False

def is_skew_left(P:PohonBiner):
    if is_one_elmt(P) or is_tree_empty(P):
        return False
    else:
        if is_uner_left(P):
            if is_one_elmt(left(P)):
                return True
            else:
                if is_uner_left(left(P)):
                    return is_skew_left(left(P))
                else:
                    return False
        else:
            return False

def is_skew_right(P:PohonBiner):
    if is_one_elmt(P) or is_tree_empty(P):
        return False
    else:
        if is_uner_right(P):
            if is_one_elmt(right(P)):
                return True
            else:
                if is_uner_right(right(P)):
                    return is_skew_right(right(P))
                else:
                    return False
        else:
            return False
# ==============================================================================
# Fungsi Lain
def level_of_X(P:PohonBiner, X:int):
    if not is_member(P, X):
        return 0
    else:
        if akar(P) == X:
            return 1
        else:
            if is_biner(P):
                return 1 + level_of_X(left(P), X) + level_of_X(right(P), X)
            elif is_uner_left(P):
                return 1 + level_of_X(left(P), X)
            elif is_uner_right(P):
                return 1 + level_of_X(right(P), X)
# ==============================================================================
# Operasi Lain
def add_leftmost_leaf(P:PohonBiner, X:int):
    """Adding Leaf (Node) X to leftmost Leaf in the Tree P

    Parameters
    ----------
    P : PohonBiner
        Tree
    X : int
        Leaf (Node)

    Returns
    -------
    PohonBiner
        New PohonBiner with added Node
    """
    if is_tree_empty(P):
        return makePB(X)
    else:
        if is_tree_empty(left(P)):
            return makePB(akar(P), makePB(X), right(P))
        else:
            return makePB(akar(P), add_leftmost_leaf(left(P), X), right(P))

def add_rightmost_leaf(P:PohonBiner, X:int):
    if is_tree_empty(P):
        return makePB(X)
    else:
        if is_tree_empty(right(P)):
            return makePB(akar(P), left(P), makePB(X))
        else:
            return makePB(akar(P), left(P), add_rightmost_leaf(right(P), X))

def add_leaf(P:PohonBiner, X:int, Y:int, Left:bool) -> PohonBiner:
    """Adding Leaf (Node) Y to Leaf X

    Parameters
    ----------
    P : PohonBiner
        Non-Epty PohonBiner
    X : int
        Pre-Existed Leaf in Tree
    Y : int
        New Leaf
    left : bool
        True for adding to Left, False for adding to Right

    Returns
    -------
    PohonBiner
        New PohonBiner with added Leaf
    """
    if akar(P) == X:
        if Left:
            return add_leftmost_leaf(P, Y)
        else:
            return add_rightmost_leaf(P, Y)
    else:
        if is_biner(P):
            if is_member(left(P), X):
                return makePB(akar(P), add_leaf(left(P), X, Y, Left), right(P))
            else:
                return makePB(akar(P), left(P), add_leaf(right(P), X, Y, Left))
        elif is_uner_left(P):
            return makePB(akar(P), add_leaf(left(P), X, Y, Left), right(P))
        elif is_uner_right(P):
            return makePB(akar(P), left(P), add_leaf(right(P), X, Y, Left))

def del_leftmost_leaf(P:PohonBiner) -> list:
    """Delete the Leftmost Leaf of PohonBiner

    Parameters
    ----------
    P : PohonBiner
        Non-Empty PohonBiner

    Returns
    -------
    list
        [PohonBiner, Leftmost_Leaf:int]
    """
    def leftmost_leaf(P:PohonBiner):
        if is_one_elmt(P):
            return akar(P)
        else:
            if is_biner(P):
                return leftmost_leaf(left(P))
            elif is_uner_left(P):
                return leftmost_leaf(left(P))
            elif is_uner_right(P):
                return leftmost_leaf(right(P))

    def delete_leaf(P:PohonBiner): 
        # Bug saat dimasukkan ke rep_prefix()
        if is_one_elmt(P):
            return None
        else:
            if is_biner(P):
                return makePB(akar(P), delete_leaf(left(P)), right(P))
            elif is_uner_left(P):
                return makePB(akar(P), delete_leaf(left(P)), right(P))
            elif is_uner_right(P):
                return makePB(akar(P), left(P), delete_leaf(right(P)))
            else:
                return None

    return [delete_leaf(P), leftmost_leaf(P)]

def del_rightmost_leaf(P:PohonBiner) -> list:
    def rightmost_leaf(P:PohonBiner):
        if is_one_elmt(P):
            return akar(P)
        else:
            if is_biner(P):
                return rightmost_leaf(right(P))
            elif is_uner_left(P):
                return rightmost_leaf(left(P))
            elif is_uner_right(P):
                return rightmost_leaf(right(P))

    def delete_leaf(P:PohonBiner):
        if is_one_elmt(P):
            return None
        else:
            if is_biner(P):
                return makePB(akar(P), left(P), delete_leaf(right(P)))
            elif is_uner_left(P):
                # return makePB(akar(P), left(P), delete_leaf(right(P)))
                return makePB(akar(P), delete_leaf(left(P)), right(P))
            elif is_uner_right(P):
                # return makePB(akar(P), delete_leaf(left(P)), right(P))
                return makePB(akar(P), left(P), delete_leaf(right(P)))

    return [delete_leaf(P), rightmost_leaf(P)]


def del_leaf(P:PohonBiner, X:int) -> PohonBiner:
    # Bug saat dimasukkan ke rep_prefix()
    """Delete Leaf X from PohonBiner

    Parameters
    ----------
    P : PohonBiner
        Non-Empty PohonBiner
    X : int
        Leaf

    Returns
    -------
    PohonBiner
        _description_
    """
    if is_one_elmt(P) and (akar(P) == X):
        return None
    else:
        if is_biner(P):
            if is_member(left(P), X):
                return makePB(akar(P), del_leaf(left(P), X), right(P))
            else:
                return makePB(akar(P), left(P), del_leaf(right(P), X))
        elif is_uner_left(P):
            return makePB(akar(P), del_leaf(left(P), X), right(P))
        elif is_uner_right(P):
            return makePB(akar(P), left(P), del_leaf(right(P), X))

def make_leaf_list(P:PohonBiner) -> list:
    """Create List of Leaf\n
    If Tree is Empty, return empty list\n
    If Tree is not Empty, return List of Leaf

    Parameters
    ----------
    P : PohonBiner
        Tree can be empty

    Returns
    -------
    list
        List of Leaf
    """
    if is_tree_empty(P):
        return []
    else:
        if is_one_elmt(P):
            return [akar(P)]
        else:
            if is_biner(P):
                return make_leaf_list(left(P)) + make_leaf_list(right(P))
            elif is_uner_left(P):
                return make_leaf_list(left(P))
            elif is_uner_right(P):
                return make_leaf_list(right(P))

def make_list_pre_order(P:PohonBiner) -> list:
    if is_tree_empty(P):
        return []
    else:
        if is_one_elmt(P):
            return [akar(P)]
        else:
            if is_biner(P):
                return ([akar(P)] 
                        + make_list_pre_order(left(P)) 
                        + make_list_pre_order(right(P)))
            elif is_uner_left(P):
                return ([akar(P)]
                        + make_list_pre_order(left(P))
                        + [])
            elif is_uner_right(P):
                return ([akar(P)]
                        + []
                        + make_list_pre_order(right(P)))

def make_list_post_order(P:PohonBiner) -> list:
    """Belom Dibikin

    Belom Selesai
    ----------
    P : PohonBiner
        _description_

    Dikata Belom Anj
    -------
    list
        _description_
    """
    pass

def make_list_in_order(P:PohonBiner) -> list:
    """Belom Dibikin Juga

    Belom Pls
    ----------
    P : PohonBiner
        _description_

    Anying Dikata Belom
    -------
    list
        _description_
    """
    pass

def make_list_level(P:PohonBiner, N:int) -> list:
    """Belom Selesai, Masi Bingung

    Masi Bingung.
    ----------
    P : PohonBiner
        _description_
    N : int
        _description_

    Iya Belom.
    -------
    list
        _description_
    """
    if is_tree_empty(P):
        return []
    else:
        if N == 0:
            return [akar(P)]
        else:
            if is_biner(P):
                pass

if __name__ == "__main__":
    PB = makePB(
        10,
        makePB(5, makePB(2), makePB(7)), 
        makePB(15, makePB(12), makePB(17)),
    )

    PB2 = makePB(
        8,
        makePB(
            5,
            makePB(3, makePB(1)),
        ),
        makePB(
            14,
            makePB(15, makePB(9), makePB(13)),
            makePB(
                12, 
                None, 
                makePB(11, makePB(10)),
            ),
        ),
    )

    PB3 = makePB(
        5,
        makePB(
            4,
            makePB(
                3,
                makePB(2, makePB(1)),
            ),
        ),
    )

    PB4 = makePB(
        6,
        None,
        makePB(
            5,
            None,
            makePB(
                4,
                None,
                makePB(3, makePB(2), makePB(1)),
            ),
        ),
    )

    PB5 = makePB(
        10,
        makePB(
            5,
            makePB(3, makePB(2), makePB(4)),
            makePB(8, makePB(7), makePB(9)),
        ),
        makePB(
            15,
            makePB(13, makePB(12), makePB(14)),
            makePB(18, makePB(17), makePB(20)),
        ),
    )

    PB6 = makePB(
        5,
        makePB(
            3,
            makePB(2, makePB(1)),
            makePB(4),
        ),
        makePB(
            10,
            makePB(8),
            makePB(12, None, makePB(13)),
        ),
    )

    """
        UNCOMMENT TO TEST
        if found error, pls lemme know :)
    """

    # print(is_tree_empty(PB2))
    # print(is_one_elmt(PB2))
    # print(is_uner_left(left(PB2)))
    # print(is_uner_right(right(right(PB2))))
    # print(nb_elmt(PB2))
    # print(nb_daun(PB2))
    # print(rep_prefix(PB2))
    # print(is_member(PB3, 3))
    # print(is_skew_left(PB3))
    # print(is_skew_right(PB4))
    # print(level_of_X(PB2, 10))
    # print(add_leftmost_leaf(PB3, 0))
    # print(add_rightmost_leaf(PB4, 0))
    # print((PB5))
    # print((add_leaf(PB5, 4, 1, False)))
    # print(rep_prefix(add_leaf(PB5, 4, 1, True)))
    # print(del_leftmost_leaf(PB5))
    # print(del_rightmost_leaf(PB5))
    # print(del_leaf(PB5, 20))
    # print(rep_prefix(PB5))
    # print(rep_prefix(del_leaf(PB5, 17)))
    # print(make_leaf_list(PB5))
    # print(rep_prefix(PB5))
    # print(make_list_pre_order(PB5))