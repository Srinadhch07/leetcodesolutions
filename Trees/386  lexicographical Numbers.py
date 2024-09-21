class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        r = []
        current =1
        for _ in range(n):
            r.append(current)
            if current * 10 <= n:
                current *=10
            else:
                print(current,current%10)
                while current%10 == 9 or current+1 >n: 
                    print(current//10)
                    current //=10
                current +=1
        return r

"""
Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
what is lexicolgraphical order ?
Placing elements in dictionary order 
ex : ab,ac,ad,ae,bc,bd,be ... so on
In the same way we have to write a program for numbers
Process :
1. we have to iterate within range of 13
2. Add 1st number i.e, 1
3. Now we find its remaining elements 10,11,12,13 jusrt like ab,ac,ad,ae so on
4. The condition to to stop adding 1 varients is it's varient should be great than 13
5. If the 1 varient is greater then 13 then we enter into while loop where we check for two condtions 
           i. current %10 == 9 {why 9 ? because we checking for once place.since max numbers in once place are 9}
           ii. current +1 > 10 {why ? This our basic condition our appending value shouldn't exceed the given number if it is we minimize it next step}
           iii. If the any one of condition is true then reduce current value making it to single digit {current=13 ---> current=1}
6. increase the current value {current =2}
7. repeat the process

"""
