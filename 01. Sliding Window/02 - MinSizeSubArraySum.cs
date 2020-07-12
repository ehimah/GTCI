/* 
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
*/
using System;

namespace gtci
{
    public class MinSizeSubArraySum
    {
        public static int findMinSubArray(int S, int[] arr)
        {
            int windowStart = 0;
            int minimumWindowSize = Int32.MaxValue;
            int windowSum = 0;
            for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
            {
                windowSum += arr[windowEnd];

                //keep shrinking the window until it's below the target size S
                while (windowSum >= S)
                {
                    minimumWindowSize = Math.Min(minimumWindowSize, windowEnd - windowStart + 1); //+1 to include both elemnts on the edge of the window positions
                    windowSum -= arr[windowStart];
                    windowStart++; //slide the window
                }
            }
            return minimumWindowSize;
        }

        public static void Run()
        {
            int result1 = MinSizeSubArraySum.findMinSubArray(7, new int[] { 2, 1, 5, 2, 3, 2 });
            int result2 = MinSizeSubArraySum.findMinSubArray(7, new int[] { 2, 1, 5, 2, 8 });
            int result3 = MinSizeSubArraySum.findMinSubArray(8, new int[] { 3, 4, 1, 1, 6 });
            Console.WriteLine($"Smallest subarray length of size S=7: {result1}");
            Console.WriteLine($"Smallest subarray length of S=7: {result2}");
            Console.WriteLine($"Smallest subarray length of S=8: {result3}");
        }
    }
}