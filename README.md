This is a small project I did in my spare time over a couple of weekends.

It was inpsired by 3 Blue 1 Brown's video on Natural Language Information theory. At the end of the second video in that series https://www.youtube.com/watch?v=GlYgs6v2YfU&t=1s, he suggests that LLMs effectively,
and directly can be used to compress natural language.

This naturally led to me to think about how to do this rather than just googling it, I came up with the idea of using a Huffman code based on the average rank of tokens. Then using a huffman code based on the actual distribution
of predicted next tokens.

Finally I did some research online and learnt about arithmetic coding (which should obtain approximately the realised information)

To compare the encoding performance of the three methods, and to research how LLMs encode information more generally, I have done this project, with a Jupyter notebook, showing the information from each.

A particular highlight is that I created my own Huffman code generator, which was nice. I did it without relying on external tools, and tried to develop the algorithms as far as possible myself.
They are all O(n) in time I believe, which was the main goal.

Please refer tot he Juptyer Notebook for my other conclusions!
