/**
        Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
        Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
**/
using System;

namespace gtci
{
    class AverageOfSubArrayOfSizeK
    {
        public static double[] findAverages(int K, int[] arr)
        {
            double[] result = new double[arr.Length - K + 1];
            int windowStart = 0;
            double windowSum = 0;
            for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
            {
                windowSum += arr[windowEnd];
                if (windowEnd >= K - 1)
                {
                    result[windowStart] = windowSum / K;
                    windowSum -= arr[windowStart];
                    windowStart++;
                }
            }
            return result;
        }
        static void Main(string[] args)
        {
            double[] result = AverageOfSubArrayOfSizeK.findAverages(5, new int[] { 1, 3, 2, 6, -1, 4, 1, 8, 2 });
            Console.WriteLine($"Averages of subarrays of size K: { string.Join(',', result) }");
        }
    }
}
