class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans =[]
        xor_arr = [0]*(len(arr)+1)
        for i,a in enumerate(arr):
            xor_arr[i+1] = xor_arr[i]^a
        #print(or_arr)
        for left,right in queries:
            ans.append(xor_arr[left]^xor_arr[right+1])
        return ans
