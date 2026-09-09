class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # complexity O(n log n)

        triples = []
        b = 0

        while b < len(nums) - 2:
            i, e = b + 1, len(nums) - 1
            while i < e:
                if nums[b] + nums[i] + nums[e] == 0:
                    triples.append([nums[b], nums[i], nums[e]])
                    bumpi = nums[i]
                    bumpe = nums[e]
                    while nums[i] == bumpi and i < e:
                        i += 1
                    while nums[e] == bumpe and i < e:
                        e -= 1
                elif nums[b] + nums[i] + nums[e] < 0:
                    i += 1
                else:
                    e -= 1
            
            bump = nums[b]
            while b < len(nums) and nums[b] == bump:
                b += 1

        return triples