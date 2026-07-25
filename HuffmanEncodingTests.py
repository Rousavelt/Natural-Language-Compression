import HuffmanEncoding
import VerboseHuffmanEncoding

token_prob_dict = {}
token_prob_dict["Cat"] = 0.4
token_prob_dict["Sad"] = 0.2
token_prob_dict["Rob"] = 0.1
token_prob_dict["Flappy"] = 0.1
token_prob_dict["Bird"] = 0.05
token_prob_dict["Man"] = 0.05
token_prob_dict["Lol"] = 0.05
token_prob_dict["Slaps"] = 0.05


my_verbose_huffman_tree = VerboseHuffmanEncoding.create_verbose_huffman_tree(token_prob_dict)
print(f"Frequency : {my_verbose_huffman_tree.frequency}")
print(f"Values : {my_verbose_huffman_tree.values}")


print("="*40)
print("Frequencies:")
for word in token_prob_dict:
    print(f"{word} : {token_prob_dict[word]}")
print("="*40)
print("From encoding one by one from verbose tree:")
for word in token_prob_dict:
    print(f"{word} : {VerboseHuffmanEncoding.encode_from_verbose_huffman_tree(my_verbose_huffman_tree, word)}")

my_huffman_tree = HuffmanEncoding.create_huffman_tree(token_prob_dict)
print("="*40)
print("From encoding dict")
my_encoding_dict = HuffmanEncoding.get_full_code_from_huffman_tree(my_huffman_tree)
for key in my_encoding_dict:
    print(f"{key} : {my_encoding_dict[key]}")

print("="*40)
print("Fully wrapped huffman encoding function:")
my_final_encoding_dict = HuffmanEncoding.get_huffman_code_from_frequency_dict(token_prob_dict)
for key in my_final_encoding_dict:
    print(f"{key} : {my_final_encoding_dict[key]}")
