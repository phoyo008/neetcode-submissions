class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = -1 

        for i in range(len(arr) -1,-1,-1): 
            current = arr[i]
            
            arr[i]= index
            index = max(index, current)
        return arr