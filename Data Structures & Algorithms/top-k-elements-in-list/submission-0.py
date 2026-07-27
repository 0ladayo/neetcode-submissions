class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        blank_notepad = {}

        for num in nums:

            if num in blank_notepad:

                blank_notepad[num] += 1

            else:

                blank_notepad[num] = 1

        buckets = [[] for i in range(len(nums) + 1)]

        for key, value in blank_notepad.items():

            buckets[value].append(key)
        
        results = []

        for row in buckets[::-1]:

            for num in row:

                results.append(num)

                if len(results) == k:

                    return results

