def sum_of_top_two(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least two integers.")
    # Sort the array in descending and then sum first two elements also two highest numbers.
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[0] + sorted_arr[1]
def test_sum_of_top_two():
    # Test case 1: Normal case
    assert sum_of_top_two([1, 4, 2, 3, 5]) == 9
    
    # Test case 2: Array with negative numbers
    assert sum_of_top_two([-10, -20, -5, -30]) == -15
    
    # Test case 3: Array with mixed positive and negative numbers
    assert sum_of_top_two([-10, 20, -5, 30]) == 50
    
    # Test case 4: Array with duplicates
    assert sum_of_top_two([5, 5, 5, 5]) == 10
    
    # Test case 5: Array with only two elements
    assert sum_of_top_two([10, 20]) == 30
    
    # Test case 6: Large numbers
    assert sum_of_top_two([100000, 99999, 2, 3, 50000]) == 199999

# Running the test function
test_sum_of_top_two()
