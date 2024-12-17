# O(n) time | O(1) space - where n is the length of the input string
# The constant space is because the input string only has lowercase
# English-alphabet letters; thus, our hash table will never have more
# than 26 character frequencies.


def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx

    return -1
