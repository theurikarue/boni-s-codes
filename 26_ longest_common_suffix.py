def LongestCommonSuffix(strs):
    common_suffix = strs[0]
    for next_word in strs[1:]:
        while not next_word.endswith(common_suffix):
            common_suffix = common_suffix[1:]
    return common_suffix

print(LongestCommonSuffix(['celebration', 'opinion', 'decision', 'revision']))
