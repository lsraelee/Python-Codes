# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(story):
    # [assignment] Add your code here 
    contents = open('story.txt', 'r')
    new_contents = contents.read()
    return new_contents


def count_words():
    # [assignment] Add your code here
    texts = read_file_content('story.txt')
    ntexts = texts.split()
    result = {}
    for words in ntexts:
        if words not in result:
            result[words.lower()] = 1
        else:
            result[words.lower()] += 1
    return result


print(count_words())
