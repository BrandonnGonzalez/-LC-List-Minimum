# Without using the built in function min, write a function that finds the minimum value in a list of integers.

#Example:
# Input: [5, 1, 2, 3, 4]
# Output: 1

def find_min(lst):
    # I could sort through the list, but that will have a bad time complexity, of O(n log n ).
    # Instead, I should iterate through the list which will be O(n) at worst.
    # Write your code here
    # Initialize the minimum value with the first element of the list
    min_val = lst[0]
    
    # Iterate through the list to find the minimum value
    for num in lst:
        if num < min_val:
            min_val = num
    
    return min_val  # Return the minimum value

# Example usage
lst1 = [5, 1, 2, 3, 4]
print(find_min(lst1))  # Output: 1

lst2 = [10, 8, 2, 4, 6]
print(find_min(lst2))  # Output: 2

if __name__ == '__main__':
    # Add additional test cases or functionality if needed
    pass

    
lst = [5, 1, 2, 3, 4]
find_min(lst)
