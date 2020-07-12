/**
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
**/

using System;

namespace gtci
{
    public class MaxSumSubArrayOfSizeK
    {
        public static int findMaxSumSubArray(int K, int[] arr)
        {
            int windowSum = 0;
            int maximumSum = 0;
            int windowStart = 0;
            for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
            {
                windowSum += arr[windowEnd]; //add the next element to the window

                //we don't slide the window until we've reached the required window size of K
                if (windowEnd >= K - 1)
                {
                    maximumSum = Math.Max(maximumSum, windowSum);
                    //remove first (outgoing) element of window from the window
                    windowSum -= arr[windowStart];
                    //slide the window
                    windowStart++;
                }
            }
            return maximumSum;
        }

        public static void Run()
        {
            int result1 = MaxSumSubArrayOfSizeK.findMaxSumSubArray(3, new int[] { 2, 1, 5, 1, 3, 2 });
            int result2 = MaxSumSubArrayOfSizeK.findMaxSumSubArray(2, new int[] { 2, 3, 4, 1, 5 });
            Console.WriteLine($"Max Sum of subarrays of size K=3: {result1}");
            Console.WriteLine($"Max Sum of subarrays of size K=2: {result2}");
        }
    }

}