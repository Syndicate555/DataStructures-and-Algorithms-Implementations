from collections import Counter


# Question: Write a class that has 3 methods. The class will be able to store words as strings and be able to return the most and least repeated word.


class WordsMcWordsFaceSuperWordCounter:
    # Constructor
    def __init__(self):
        # initializing an empty array to store the words
        self.data = []

    def RecordWord(self, word):
        # Appending the word to the global array
        self.data.append(word)

    def TopWord(self):  # This method only returns the most used word
        # converting the array into a dictionary with key/value pairs
        a = dict(Counter(self.data))
        # returning the most repeated item in the dictionary
        return (max(a, key=a.get))

    def LeastWord(self):  # This method only returns the least used word
        # converting the array into a dictionary with key/value pairs
        a = dict(Counter(self.data))
        # returning the most repeated item in the dictionary
        return (min(a, key=a.get))


# Test Cases to try out my code

# Instantiate the class
test = WordsMcWordsFaceSuperWordCounter()

# Populate the class by adding words to it
test.RecordWord("pizza")
test.RecordWord("pizza")
test.RecordWord("burger")
test.RecordWord("burger")
test.RecordWord("fries")
print(test.TopWord())
print(test.LeastWord())
