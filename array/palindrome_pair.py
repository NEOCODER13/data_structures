def is_palindrome(s):
    return s == s[::-1]

def palindrome_pairs(words):
    result = []
    word_map = {word[::-1]: i for i, word in enumerate(words)}
    # reflection of the word is in the map
    for i, word in enumerate(words):
        if word in word_map and word_map[word] != i:
            result.append((i, word_map[word]))
    # empty string + palindrome
    for i, word in enumerate(words):
        if is_palindrome(word) and "" in word_map and i!=word_map[""]:
            result.append((i, word_map[""]))
            result.append((word_map[""], i))
    #prefix or suffix is palindrome
    for i, word in enumerate(words):
        for j in range (1, len(word)):
            prefix, suffix = word[:j], word[j:]
            if is_palindrome(prefix) and suffix[::-1] in word_map:
                result.append((word_map[suffix[::-1]], i))
            if is_palindrome(suffix) and prefix[::-1] in word_map:
                result.append((i, word_map[prefix[::-1]]))
    return result

print(palindrome_pairs(["bat", "tab", "cat", "tat", "", "tac", "at"]))

# complexity O(n*k*k)
