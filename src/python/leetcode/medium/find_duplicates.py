# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

# Returns, array 
# of duplicate elements

class Solution:
    def getDuplicates(self, arr):
        result = []
        for i in range(len(arr)):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                result.append(index + 1)
            arr[index] = -arr[index]            
        return result
        


if __name__ == "__main__":
    testArray = [4,3,2,7,8,2,3,1]
    instance = Solution()
    print(instance.getDuplicates(testArray))
