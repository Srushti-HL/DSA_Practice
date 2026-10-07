class Solution:
    def findAndReplacePattern(self, words, pattern):
        result = []

        def matches(word):
            pattern_to_word = {}
            word_to_pattern = {}

            for p, w in zip(pattern, word):

                # Check pattern -> word mapping
                if p in pattern_to_word:
                    if pattern_to_word[p] != w:
                        return False
                else:
                    pattern_to_word[p] = w

                # Check word -> pattern mapping
                if w in word_to_pattern:
                    if word_to_pattern[w] != p:
                        return False
                else:
                    word_to_pattern[w] = p

            return True

        for word in words:
            if matches(word):
                result.append(word)

        return result