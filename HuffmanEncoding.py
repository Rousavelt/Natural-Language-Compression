import heapq

# For this, we order a node by its frequency
# Then by the value
# Finally by identifier
# The goal is that the same input frequency dictionary should always
# Result in the same encoding
class HuffmanTree:
    def __init__(self, identifier : int, frequency : float, value : str, left, right):
        self.identifier = identifier
        self.frequency = frequency
        self.value = value
        self.left = left
        self.right = right

    def sort_key(self):
        return (self.frequency, self.value, self.identifier)

    def __lt__(self, other):
        if not hasattr(other, "frequency") or not hasattr(other, "value") or not hasattr(other, "identifier"):
            return NotImplemented
        return self.sort_key() < other.sort_key()

def create_huffman_tree(value_frequency_dict : dict) -> HuffmanTree:
    nodes = []
    j = 0 # For assigning identifiers to nodes
    for key in value_frequency_dict:
        new_node = HuffmanTree(j, value_frequency_dict[key], key, None, None)
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
        new_node = HuffmanTree(j, right_node.frequency + left_node.frequency, "", left_node, right_node)
        j += 1
        heapq.heappush(nodes, new_node)
    
    return heapq.heappop(nodes)


def get_full_code_from_huffman_tree(huffmantree: HuffmanTree) -> dict:
    # Explore using stack.

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
            codeword_dict[current_node.value] = sub_codeword_identifier_dict[current_node.identifier]
    
    return codeword_dict


def get_huffman_code_from_frequency_dict(value_frequency_dict : dict) -> dict:
    huffman_tree = create_huffman_tree(value_frequency_dict)
    return get_full_code_from_huffman_tree(huffman_tree)
