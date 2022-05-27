# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    #removing spaces
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

#if word and anagram are thesame
    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return False


# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("anagram", "Nag a ram"))
print(find_anagram("race", "care"))

