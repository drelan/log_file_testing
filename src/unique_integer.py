def find_single_integer(mixed_list):
    # Use a dictionary to count integer occurrences only
    int_counts = {}
    for item in mixed_list:
        if isinstance(item, int):  # Only process integers
            int_counts[item] = int_counts.get(item, 0) + 1
    
    # Find the integer that appears exactly once
    for integer, count in int_counts.items():
        if count == 1:
            return integer
    
    return None  # Return None if no single integer found

if __name__ == "__main__":
    # Example usage
    test_list = [3, 'a', 0, 'b', -1, 3, 0, -1, 9]
    result = find_single_integer(test_list)
    print(f"The integer appearing once in {test_list} is: {result}")
