class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string in the list sort them and then create a set
        # remember the indexes of the same words
        wordSet = {}
        wordArrays = []
        for i, word in enumerate(strs):
            print(i, word)
            sortWord = sorted(list(word))
            sortWord = ('').join(sortWord)
            if sortWord not in wordSet:
                wordSet[sortWord] = []
            wordSet[sortWord].append(i)
        for word in wordSet:
            curr = []
            for i in wordSet[word]:
                curr.append(strs[i])
            wordArrays.append(curr)
        return wordArrays
        
