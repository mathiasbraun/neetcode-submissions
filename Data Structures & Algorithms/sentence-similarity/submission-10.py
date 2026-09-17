class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        check = set()
        for pair in similarPairs:
            check.add(tuple(pair))
        
        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            if ((sentence1[i], sentence2[i]) not in check and (sentence2[i], sentence1[i]) not in check and sentence1[i] != sentence2[i]):
                return False
        return True