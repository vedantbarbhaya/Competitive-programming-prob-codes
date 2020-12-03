"""
PROBLEM - MIN NO. OF OPERATIONS TO MAKE ALL ELEMENTS IN EQUAL

AN ARRAY IS GIVEN IN WHICH EACH ELEMENT = ((2*i)+1) WHERE i IS THE INDEX. YOU CAN ADD A 1 TO AN ELEMENT OR SUBTRACT 1 FROM ANOTHER ELEMENT IN EACH STEP. FIND THE MIN NUMBER OF STEPS REQUIRED TO MAKE ALL ELEMENTS OF THE ARRAY EQUAL.

INPUT: no. of elements in the array

EXAMPLE: [3,5,7]

minimum steps = 4

3 + 2 = 5 and 7- 2 = 5
"""
class Solution:
    def minOperations(self, no: int) -> int:

        n = []
        for i in range(no):
            n.append((2*i)+1)


        if len(n) % 2 != 0:
            mid =  int(len(n) /2)
            tar = n[mid]

        else:
           mid = int(len(n)/2) - 1

           tar = ((n[mid] + n[mid+1]) / 2)


        steps = 0

        if len(n) % 2 != 0:
            for i in range(mid):
                steps = steps + (tar - n[i])
            steps = steps * 2



        if len(n) % 2 == 0:
            for i in range(mid+1):
                steps = steps + (tar - n[i])
            steps = steps *2


        return int(steps)
    
