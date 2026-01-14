def longestCommonPrefix(strs):
    # if list is empty, no prefix
    if not strs:
        return ""

    # start with the first word as the prefix
    prefix = strs[0]

    # compare prefix with every other word
    for word in strs[1:]:
        # reduce prefix until it matches the start of 'word'
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # remove last character
            if prefix == "":      # if prefix becomes empty, stop
                return ""
    
    return prefix


# Example test
words = ["flower", "flow", "flight"]
print("Longest common prefix is:", longestCommonPrefix(words))
