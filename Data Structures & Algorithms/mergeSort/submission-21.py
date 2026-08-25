class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 0:
            return []
        
        start = 0
        end = len(pairs) - 1

        if end - start + 1 <= 1:
            return pairs

        middle = (start + end)//2

        merge = []
        leftlist = self.mergeSort(pairs[start:middle + 1])
        rightlist = self.mergeSort(pairs[middle + 1:end + 1])

        i, j = 0, 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i].key <= rightlist[j].key:
                merge.append(leftlist[i])
                i += 1
            else:
                merge.append(rightlist[j])
                j += 1

        if i < len(leftlist):
            for k in range(i,len(leftlist)):
                merge.append(leftlist[k])

        if j < len(rightlist):
            for l in range(j,len(rightlist)):
                merge.append(rightlist[l])      

        return merge