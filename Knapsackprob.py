"--------GREEDY APPROACH---------"


class Solution:

    def knapsack(self,weight,profit,cap):
            ratio = [0 for x in range(len(weight))]
            ratio = [v/w for v, w in zip(profit, weight)]

            index = list(range(len(weight)))
            # sort index based on the values in the ratio
            index.sort(key=lambda i: ratio[i], reverse=True)

            fractions = [0]*len(profit)
            prof = 0
            for i in index:

                if cap == 0:
                    break

                if weight[i] <= cap:
                    prof += profit[i]
                    cap -= weight[i]
                    fractions[i] = 1

                elif weight[i] > cap:
                    fractions[i] = cap/weight[i]
                    prof += ratio[i]*cap
                    cap -= cap


            return prof,fractions

a = Solution()
profit, fract = a.knapsack([2,3,5,7,1,4,1],[10,5,15,7,6,18,3],15)
print(profit,fract)





"--------DP APPROACH---------"
'''
For this we use 0/1 method. That is we dont take fractions of an item. We either
take the entire item or we dont.
'''


weights = [5,4,6,3]
profit = [10,40,30,50]
W = 10
l = len(weights)
knap = [[0 for x in range(W + 1)] for x in range(l + 1)]
print(knap)


for i in range(l+1):
    for j in range(W+1):

        if i== 0 or j == 0:
            knap[i][j] = 0

        # if the weight of the current item is less than remaining capacity, we have
        # the option to include it, if it potentially increases the maximum obtainable
        # value. The maximum obtainable value by including item i is thus = the value
        # of item i itself + the maximum value that can be obtained with the
        # remaining capacity of the knapsack = profit[i-1] + knap[i-1][j-weights[i-1]].
        # we have done profit[i-1] and weights[i-1] for curr item to account for the
        # extra row and column in knap array


        elif weights[i-1] <= j:
            knap[i][j] = max(profit[i-1] + knap[i-1][j-weights[i-1]],knap[i-1][j])

        # if the weight of current item is greater than the remaining capacity
        # than the max we can carry is the maximum without adding the current
        # item which is present in knap[i-1][j]
        else:
            knap[i][j] = knap[i-1][j]


    print(knap)



"--------SPACE OPTIMIZED DP APPROACH---------"
