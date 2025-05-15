using System;

class binarySearch
{
    static int Main()
    {
        int[] data = {1, 3, 4, 6, 8, 10, 13};   // Binary Search must have a sorted list
        int target = 8; // Value we want to find in the list
        
        int left = 0;   // Initializing the first element in the array
        int right = data.Length - 1;    // Initializing the last element's index
        
        while(left <= right)    // Loop repeats while there's still elements to search through
                                // If left is greater than or passes right, there's nothing to search
        {
            int mid = left + (right - left) / 2;    // Initializing the calculation of the middle index
            
            if(data[mid] == target) // If middle item equals target....
            {
                Console.WriteLine(data[mid]);   // Print out target
                return 0;   // Ends program since we found what we were looking for
            }

            else if(data[mid] < target) // If middle item is less than target item....
            {
                left = mid + 1; // We look at only the right side and removing left side including the middle item -- one spot to the right of middle
            }
                
            else
            {
                right = mid - 1;   // We look at only the left side and removing right side including the middle item -- one spot to the left of middle 
            }
        }
        
        Console.WriteLine("Target Not Found."); // If target doesn't exit in the array, print....
        return 1;   // End program with failure
    }
    
}