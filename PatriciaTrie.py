
from Util import Util


class Node:
    def __init__(self, key, children, is_leaf=True, value=None):
        """
        Basic element of the Trie
        :param key: The key of the node
        :param children: List of children nodes
        :param is_leaf: Is current node leaf or not, default=False
        :param value: Value of the node
        """
        self.key = key
        self.children = children
        self.is_leaf = is_leaf
        self.value = value

    def __str__(self):
        result = self.key
        if self.children:
            result += " -> ["
            for child in self.children:
                if child.key:
                    result += str(child)
                    result += ", "
            result = result[:-2] + "]"
        return result

    def __repr__(self):
        result = self.key
        if self.children:
            result += " -> ["
            for child in self.children:
                if child.key:
                    result += str(child)
                    result += ", "
            result = result[:-2] + "]"
        return result

    def add(self, word, value):
        """
        Add a Node with the given as the prefix key
        and the value in the, if the word already
        exists the value is unioned with the existing
        word's value
        :param word: The word to add in
        :param value: The value to add for the Node
        :return: True if added successfully else None
        """
        prefix = Util.get_prefix(self.key, word)

        """
        if current node matches the prefix we already have that word
        """
        if prefix == word:
            if self.value:
                self.value = self.value.union(value)
            else:
                self.value = value
            return True

        """
        If current node is leaf and we need to add another leaf node,
        split the current node
        """
        if self.is_leaf:
            if prefix:
                self.children.append(Node(self.key[len(prefix):], list(), value=self.value))
            self.children.append(Node(word[len(prefix):], list(), value=value))
            self.key = prefix
            self.is_leaf = False
            return True

        """
        Check if word can be traced with current internal nodes
        """
        if self.children:
            for child in self.children:
                if not prefix and Util.has_prefix(child.key, word):
                    return child.add(word, value)
                if Util.has_prefix(child.key, word[len(prefix):]):
                    return child.add(word[len(prefix):], value)

        """
        Add new external nodes
        """
        if not prefix:
            self.children.append(Node(word, list(), value=value))
        elif prefix != self.key:
            new_node = Node(word[len(prefix):], list(), value=value)
            new_child_node = Node(self.key[len(prefix):], self.children, is_leaf=False)
            self.children = list()
            self.children.append(new_child_node)
            self.children.append(new_node)
            self.key = prefix
        else:
            self.children.append(Node(word[len(prefix):], list(), value=value))

        self.is_leaf = False
        return True

    def search(self, word):
        """
        Recursively search a word in the from this Node
        :param word: The word to search
        :return: The node where the word matches after
        tracing from the root else None
        """
        prefix = Util.get_prefix(self.key, word)

        if prefix == word:
            return self

        if self.is_leaf:
            return None

        if self.children:
            for child in self.children:
                if not prefix and Util.has_prefix(child.key, word):
                    return child.search(word)
                if Util.has_prefix(child.key, word[len(prefix):]):
                    return child.search(word[len(prefix):])


Trie = Node("#", list(), is_leaf=False) # Inverted Index file 
