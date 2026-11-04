class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ''' Solution with O(n^2) time, O(1) space
        arr = [0 for i in range(len(temperatures))]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                arr[i] += 1
                if temperatures[j] > temperatures[i]:
                    break
                if (j == len(arr) - 1 and 
                    temperatures[j] <= temperatures[i]):
                    arr[i] = 0          
        
        return arr'''

        output = [0 for i in range(len(temperatures))]
        # Stack contains pair [temp, index]
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                output[stack_index] = i - stack_index
            stack.append([t, i])

        return output