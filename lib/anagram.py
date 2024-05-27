# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        sorted_word = sorted(self.word)
        return [word for word in words if sorted(word.lower()) == sorted_word and word.lower() != self.word]
