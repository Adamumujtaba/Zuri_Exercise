# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
      contents = f.read()
      print(contents)
print(read_file_content("./story.txt"))
    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = dict()
    text = str.split()

    for x in text:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


    return {"as": 10, "would": 20}