import functools


class ReverseTrie:
    class TrieNode:
        def __init__(self, c=None, root=False, term=False):
            self.root, self.term = root, term
            self.children = []
            self.c = c
            self.count = 1
        def __iter__(self):
            return self.children
        def __contains__(self, item):
            return item in self.children
        def __repr__(self):
            return self.c
        def __str__(self):
            return self.c
    def __init__(self, words):
        self.root = self.TrieNode(root=True)
        for word in words:
            self.add(word)
    def add(self, word):
        """Add (reversed) word char-by-char to trie."""
        node = self.root
        for c in reversed(word):
            found = False
            for n in node.children:
                if n.c == c:
                    n.count += 1
                    found = True
                    node = n
            if not found:
                # Create new node.
                n = self.TrieNode(c)
                node.children.append(n)
                node = n
        # Append terminating node.
        node.children.append(self.TrieNode(term=True))
    def nrhymes(self, node=None):
        # Root condition: only count paired words.
        if not node:
            total_paired = 0
            for child in self.root.children:
                paired, unpaired = self.nrhymes(child)
                assert paired % 2 == 0
                total_paired += paired
            return total_paired
        # Terminating condition
        if node.term == True:
            return 0, 1
        # Recurse through children to find pairs.
        total_paired, total_unpaired = 0, 0
        for child in node.children:
            paired, unpaired = self.nrhymes(child)
            total_paired += paired
            total_unpaired += unpaired
        if total_unpaired >= 2:
            # Two or more words share the same pivot/accent letter, therefore
            # we can only count 2.
            total_paired += 2
            total_unpaired -= 2
        return total_paired, total_unpaired

def alien_rhyme(words):
    """
    ...
    """
    rtrie = ReverseTrie(words)
    nrhymes = rtrie.nrhymes()
    return nrhymes

def main():
    """Take input from standard in, and push results to standard out."""
    # Read line giving number of examples
    t = int(input())
    for i in range(1, t + 1):
        # Collect words.
        nwords = int(input())
        words = []
        for j in range(nwords):
            words.append(input())
        # Compute answer.
        nrhymes = alien_rhyme(words)
        # Push results to standard out
        print("Case #{}: {}".format(i, nrhymes))

# Run with command `python function.py < input.txt`.
main()