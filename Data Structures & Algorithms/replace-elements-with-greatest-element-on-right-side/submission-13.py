class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # for i in range(len(arr)-1):
        #    arr[i] = max(arr[i+1:])
        # arr[len(arr)-1] = -1
        # return arr
        # This has complexity O(n^2)

        max_right = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            save = arr[i]
            arr[i] = max_right
            max_right = max(max_right, save)
        arr[len(arr)-1] = -1
        return arr