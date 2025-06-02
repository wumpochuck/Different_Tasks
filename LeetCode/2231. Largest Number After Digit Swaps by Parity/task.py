"""
You are given a positive integer num. You may swap any two digits of num that have the same 
parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

Constraints:

    1 <= num <= 10^9
"""

class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)

        even = [] # четные
        odd = [] # нечетные
        for i in s:
            even.append(i) if int(i) % 2 == 0 else odd.append(i)

        even.sort(reverse=True)
        odd.sort(reverse=True)
        even_index = 0
        odd_index = 0

        ss = ""
        for i in s:
            if int(i) % 2 == 0:
                ss += even[even_index]
                even_index += 1
            else:
                ss += odd[odd_index]
                odd_index += 1
        return int(ss)
    

solution = Solution()
print(solution.largestInteger(1234))
print(solution.largestInteger(65875))
