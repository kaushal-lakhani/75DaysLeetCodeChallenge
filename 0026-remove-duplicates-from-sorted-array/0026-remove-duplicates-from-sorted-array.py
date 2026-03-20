class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        ptr = 0
        ctn = 1
        for i in range(1, len(arr)):
           
            if arr[i] != arr[ptr]:
                ctn+=1                
                ptr+=1
                arr[ptr] = arr[i]
        return ctn