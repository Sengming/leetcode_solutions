class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def find_from_order(char, order):
            for i in range(0, 26):
                if char == order[i]:
                    return i

            # error
            print("error")
            return -1

        def compare(word1, word2, order):
            # if word1 < word2
            #    return true
            # else
            #    return false
            for i in range(0, min(len(word1), len(word2))):
                if find_from_order(word1[i], order) < find_from_order(word2[i], order):
                    return True
                elif find_from_order(word1[i], order) > find_from_order(word2[i], order):
                    return False
                else:
                    continue

            if len(word1) > len(word2):
                return False

            return True

        for i in range(0, len(words)-1):
            if compare(words[i], words[i+1], order) == False:
                return False

        return True
