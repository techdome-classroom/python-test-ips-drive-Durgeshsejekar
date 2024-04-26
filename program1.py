


from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:
    # Filter out non-positive integers
    nums = [num for num in nums if num > 0]
    
    # Create a set for quick lookup
    nums_set = set(nums)
    
    # Initialize smallest_missing
    smallest_missing = 1
    
    # Iterate from smallest_missing upwards
    while True:
        if smallest_missing not in nums_set:
            return smallest_missing
        smallest_missing += 1










    



  

