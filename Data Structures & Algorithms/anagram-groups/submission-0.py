class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        blank_notepad = {}

        for word in strs:

            sorted_word = ''.join(sorted(word))

            if sorted_word in blank_notepad:
                
                 blank_notepad[sorted_word].append(word)
            
            else:

                blank_notepad[sorted_word] = [word]

        return list(blank_notepad.values())
        