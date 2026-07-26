class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        blank_notepad = set()

        for num in nums:

            if num in blank_notepad:

                return True

            else: 

                blank_notepad.add(num)
        
        return False
        