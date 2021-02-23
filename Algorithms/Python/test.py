from collections import Counter


class Words:
    def __init__(self):
        self.data = []

    def record(self, string):
        self.data.append(string)

    def TopWord(self):
        a = dict(Counter(self.data))
        return(max(a, key=a.get))

    def LeastWord(self):
        a = dict(Counter(self.data))
        return(min(a, key=a.get))


d = Words()
d.record('Saffat')
d.record('Saffat')
d.record('Saffat')
d.record('Aziz')
d.record('Aziz')
d.record('Raiyan')
print(d.TopWord())
print(d.LeastWord())


# Importing Counter from collections library


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
