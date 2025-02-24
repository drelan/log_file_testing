# unique_integer.py
def unique_integer_check(list_integers):
    for i in list_integers:
        if list_integers.count(i) == 1:
            return True
    return False  # Explicitly return False if no unique integer is found

if __name__ == "__main__":
    # Example usage when running standalone
    test_list = [3, 0, -1, 9, 3, 0, -1]
    result = unique_integer_check(test_list)
    print(f"Does the list {test_list} have a unique integer? {result}")
