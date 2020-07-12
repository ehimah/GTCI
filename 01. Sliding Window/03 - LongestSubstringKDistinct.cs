/* 
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi". */
using System;
using System.Collections.Generic;
namespace gtci
{
    public class LongestSubstringKDistinct
    {
        public static int findLength(string str, int k)
        {
            int longestLength = 0;
            int windowStart = 0;
            var frequencyMap = new Dictionary<char, int>();
            for (int windowEnd = 0; windowEnd < str.Length; windowEnd++)
            {
                char endChar = str[windowEnd];
                frequencyMap[endChar] = frequencyMap.GetValueOrDefault(endChar, 0) + 1;

                //we only shrink the sliding window when we have more than k elements; shrink until we have k characters left
                while (frequencyMap.Count > k)
                {
                    char startChar = str[windowStart];
                    frequencyMap[startChar] = frequencyMap[startChar] - 1;
                    if (frequencyMap[startChar] == 0) frequencyMap.Remove(startChar);
                    windowStart++;
                }
                //we will always calculate the maximum length whether or not we've hit the frequency count limit
                longestLength = Math.Max(longestLength, windowEnd - windowStart + 1);
            }
            return longestLength;
        }

        public static void Run()
        {
            int result1 = LongestSubstringKDistinct.findLength("araaci", 2);
            int result2 = LongestSubstringKDistinct.findLength("araaci", 1);
            int result3 = LongestSubstringKDistinct.findLength("cbbebi", 3);
            Console.WriteLine($"Length of the longest substring: S=2: {result1}");
            Console.WriteLine($"Length of the longest substring: S=1: {result2}");
            Console.WriteLine($"Length of the longest substring: S=3: {result3}");
        }
    }
}