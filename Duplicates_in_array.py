"""
PROBLEM: Find All Duplicates in an Array

Statement: Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

"""


'''
Approach: The basic idea is to use a HashMap to solve the problem but we are not suppose to use extra space, that means we will have to use our array as hashmap if we want to use a hashmap.

If we notice, the numbers in the array are from 0 to n-1, and the input array has  length n. So, the input array can be used as a HashMap.

While Traversing the array, if an element ‘a’ is encountered then increase the  value of a%n‘th element by n. The frequency can be retrieved by dividing the a % n’th element by n.

Algorithm:

    Traverse the given array from start to end.
    For every element in the array increment the arr[i]%n‘th element by n.
    Now traverse the array again and print all those indexes i for which arr[i]/n is greater than 1. Which guarantees that the number n has been added to that index
    This approach works because all elements are in the range from 0 to n-1 and arr[i] would be greater than n only if a value “i” has appeared more than once.

'''

# Python3 code to find duplicates in O(n) time

numRay = [4,3,2,7,7,2,3,1];
arr_size = len(numRay);
for i in range(arr_size):

    numRay[numRay[i] % arr_size] = numRay[numRay[i] % arr_size] +arr_size;

print("The repeating elements are : ");
for i in range(arr_size):
    if (numRay[i]/arr_size >= 2):
        print(i, " ");
