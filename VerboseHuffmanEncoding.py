import heapq
import functools

@functools.total_ordering
class VerboseHuffmanTree:
    def __init__(self, identifier : int, frequency : float, values : set, left, right):
        self.identifier = identifier
        self.frequency = frequency
        self.values = values
        self.left = left
        self.right = right

    def _is_valid_operand(self, other):
        return (hasattr(other, "frequency"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.frequency == other.frequency
    
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.frequency < other.frequency

def create_verbose_huffman_tree(value_frequency_dict : dict) -> VerboseHuffmanTree:
    nodes = []
    j = 0 # For assigning identifiers to nodes
    for key in value_frequency_dict:
        values_set = set()
        values_set.add(key)
        new_node = VerboseHuffmanTree(j, value_frequency_dict[key], values_set, None, None)
        j += 1
        nodes.append(new_node)
    n = len(nodes)

    if n == 0:
        raise ValueError("There must be at least one item in the value-frequency dictionary")


    heapq.heapify(nodes)

    # We remove one node from the list at each step.
    # There are n nodes, we want to remove them all (keeping the final node as the tree)
    # So there are n steps
    

    for i in range(n-1): # We combine the least likely nodes at each stage, and insert back into the heap
        right_node = heapq.heappop(nodes)
        left_node = heapq.heappop(nodes)
        new_node = VerboseHuffmanTree(j, right_node.frequency + left_node.frequency, set.union(right_node.values, left_node.values), left_node, right_node)
        j += 1
        heapq.heappush(nodes, new_node)
    
    return heapq.heappop(nodes)

# If using once then this is fine.
# However if we repeatedly use the tree, it's better to put it into a dictionary
# Also the storage with the Verbose tree is a bit inefficient, though easier for debugging
# Each value will be stored based on its depth in the tree
# Which approximately scales with the log. So the storage is appoximately nlog(n) rather than n.
# If we didn't store 'directions' with the values at each node in the tree.
def encode_from_verbose_huffman_tree(huffmantree : VerboseHuffmanTree, encoding_value):
    if encoding_value not in huffmantree.values:
        raise ValueError("The value to encode must be in the VerboseHuffmanTree")
    
    current_node = huffmantree
    code_string = ""

    if len(current_node.values) == 1:
        return "1" # We use 1 for left, 0 for right

    while len(current_node.values) > 1:
        if encoding_value in current_node.left.values:
            code_string += "1"
            current_node = current_node.left
        else:
            code_string += "0"
            current_node = current_node.right

    return code_string

def get_full_code_from_verbose_huffman_tree(huffmantree: VerboseHuffmanTree) -> dict:
    # Each node in the tree has two branches. Left or right.
    # Therefore in order to explore, we will encounter each
    # node three times. Once when we initially encounter, and 
    # go left. Once when coming back up to go right. And then
    # Once when returning.

    node_stack = []
    node_stack.append(huffmantree)

    sub_codeword_identifier_dict = dict() # Store the sub codeword at each point in the tree
    sub_codeword_identifier_dict[huffmantree.identifier] = ""

    # Explore the tree, extending sub codewords, or codewords when leaves reached

    codeword_dict = dict()
    while (len(node_stack) > 0):
        current_node = node_stack.pop()
        if current_node.right != None:
            node_stack.append(current_node.right)
            sub_codeword_identifier_dict[current_node.right.identifier] = sub_codeword_identifier_dict[current_node.identifier] + "0"
        if current_node.left != None:
            node_stack.append(current_node.left)
            sub_codeword_identifier_dict[current_node.left.identifier] = sub_codeword_identifier_dict[current_node.identifier] + "1"
        if current_node.right == None and current_node.left == None:
            codeword_dict[next(iter(current_node.values))] = sub_codeword_identifier_dict[current_node.identifier]
    return codeword_dict
