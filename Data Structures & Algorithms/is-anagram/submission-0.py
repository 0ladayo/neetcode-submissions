class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        blank_notepad = {}

        for char in s:

            if char in blank_notepad:

                blank_notepad[char] += 1

            else:

                blank_notepad[char] = 1

        for char in t:

            if char in blank_notepad:

                if blank_notepad[char] == 0:

                    return False

                else:

                    blank_notepad[char] -= 1

            else:

                return False
        
        return True



        