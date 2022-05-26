# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    srted_word = sorted(word)
    srted_anagram = sorted(anagram)
    if len(word) == len(anagram) and srted_word == srted_anagram:
        return True
    else:
        return False


first_check = find_anagram("hello", "check")
second_check = find_anagram("below", "elbow")
print('find_anagrams("hello", "check") --> ' + str(first_check))
print('find_anagrams("hello", "check") --> ' + str(second_check))
