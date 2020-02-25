'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
'''
# read in the text file with our word list

file = open('words.txt', 'r')
words = file.read().split("\n")
file.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# Good question to think about: how to represent the word list in a way that we can search it efficiently?


def buggy_swap(word, letter, rune):
    word_as_list = list(word)
    # what if we are trying to swap the second 'i' in 'india'?
    # we will always get 0 for the index!
    # we can fix this by passing in the index to use
    letter_index = word_as_list.index(letter)

    word_as_list[letter_index] = rune

    new_word = "".join(word_as_list)

    return new_word


def swap(word, index, char):
    word_as_list = list(word)
    word_as_list[index] = char
    new_word = "".join(word_as_list)

    return new_word


def getNeighbors(word):
    # if a word is one letter different
    # and if it's in the list of words
    # it's a neighbor

    # change a letter and make a potential word
    # if it's in our word_set, it's a neighbor!

    neighbors = []

    # range gives us an array: [0, 1, 2, 3, 4]
    # we can use the index to be sure we are swapping the right letter!
    for index in range(len(word)):
        letter = word[index]
        for char in alphabet:
            if letter != char:
                maybe_word = swap(word, index, char)
                if maybe_word in word_set:
                    neighbors.append(maybe_word)

    return neighbors

# good question: how does this work with getNeighbors
# and enable us to treat a giant word list as a GRAPH?

# run breadth first search


def find_word_ladder(start_word, end_word):
    queue = Queue()
    visited = set()
    queue.enqueue([start_word])

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]

        if current_node == end_word:
            return current_path

        if current_node not in visited:
            visited.add(current_node)

            edges = getNeighbors(current_node)

            for edge in edges:
                path_copy = list(current_path)
                path_copy.append(edge)
                queue.enqueue(path_copy)


print(find_word_ladder("sail", "boat"))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)
