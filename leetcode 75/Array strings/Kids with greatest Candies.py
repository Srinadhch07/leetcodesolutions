class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        d_candies=[i+extraCandies for i in candies]
        print(d_candies)
        result=[]
        for i in d_candies:
            temp=[]
            for j in candies:
                if i >= j:
                    temp.append(True)
                else:
                    temp.append(False)
            #print(temp)
            if all(temp):
                result.append(True)
            else:
                result.append(False)
            temp=[]
        print(result)

        return result
