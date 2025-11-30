def handle_full_node(self, debug=True):
    """Try to lend a key to left or right sibling if they have < 2*self.d keys.

       Otherwise, split the node into two.

    
    Return value:
    
        If we can successfully lend the key/pointer to either sibling, return None
        Otherwise, return whatever result self.split_node_into_two() does.
    """
    # use debug key to print useful messages for your debugging
    assert len(self.keys) == 2 * self.d + 1

    d = self.d

    if self.parent == None : # already at the root
        return self.split_node_into_two() # no other option but to split

    # unpack the parent pointer
    (parent_node, parent_idx) = self.parent

    # self is the child of parent_node and equals parent_node.pointers[parent_idx]
    ## TODO:
    ##   1. Check if I have a right sibling node, fetch right sibling node and find out if it has space.
    ##        1.1. If right sibling exists and has space, lend my rightmost key and pointer to the right sibling as its leftmost key and pointer
    ##        1.2 Do not forget to call the function fix_parent_pointers since parent pointers will get invalidated.
    ##        1.2 Insertion is done, return None
    
    ##   2. Check if I have a left sibling node, fetch left sibling node and find out if it has space
    ##        2.1 If left sibling exists and has space, lend my leftmost key and pointer to left sibling as its rightmost key and pointer 
    ##        3.3 Insertion is done, return None
    ##   3. If neither options work, return self.split_node_into_two() -- already implemented see above.
    ##  Look at the deletion code for B-Tree given in the notes first since it uses a similar (but not the same) strategy.
    
    # your code here
    if self.lend_right(parent_node, parent_idx) or self.lend_left(parent_node, parent_idx):
        return None

    return self.split_node_into_two()


def lend_right(self, p_node, p_index):
    if p_index >= len(p_node.pointers) - 1:
        return False
    
    right_sibling = p_node.pointers[p_index + 1]
    
    if len(right_sibling.keys) >= 2 * self.d:
        return False

    separator_idx = p_index 
    parent_separator = p_node.keys[separator_idx]

    my_max_key = self.keys.pop()
    p_node.keys[separator_idx] = my_max_key
    right_sibling.keys.insert(0, parent_separator)

    if not self.is_leaf():
        right_sibling.pointers.insert(0, self.pointers.pop())
        right_sibling.pointers[0].parent = (right_sibling, 0)
        right_sibling.fix_parent_pointers_for_children()

    return True

def lend_left(self, p_node, p_index):
    if p_index <= 0:
        return False
        
    left_sibling = p_node.pointers[p_index - 1]

    if len(left_sibling.keys) >= 2 * self.d:
        return False

    separator_idx = p_index - 1
    parent_separator = p_node.keys[separator_idx]

    my_min_key = self.keys.pop(0)
    p_node.keys[separator_idx] = my_min_key
    left_sibling.keys.append(parent_separator)

    if not self.is_leaf():
        left_sibling.pointers.append(self.pointers.pop(0))
        left_sibling.pointers[-1].parent = (left_sibling, len(left_sibling.pointers) - 1)
        self.fix_parent_pointers_for_children()

    return True