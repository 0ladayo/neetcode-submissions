class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        blank_notepad = {}

        for index, num in enumerate(nums):

            needed_number = target - num

            if needed_number in blank_notepad:

                return [blank_notepad[needed_number], index]

            else:

                blank_notepad[num] = index
        