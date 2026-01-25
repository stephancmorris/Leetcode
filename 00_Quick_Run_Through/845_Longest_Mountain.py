class Solutuin:
    def LongestMountain(self, arr: List[int]) -> int:
        result = 0 

        for i in range(1, len(arr) - 1): # loop accouting for the peak 
            if arr[i-1] < arr[i] > arr[i+1]: #checks if peak with numbers next to it
                l = r = i #assign pointers for search party 
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1
                while r < len(arr) - 1 and arr[r] > arr[r] + 1:
                    r += 1
                
                result = max(result, r - 1 + 1)
        return result


