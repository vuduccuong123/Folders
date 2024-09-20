from collections import Counter
# arr = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'cc']
def most_tring_lengths_frequency(arr):
    # Step 1: Calculate the lengths of each string in the array:
    # For exmaple in put array ['a','ab','abc','cd','def','gh'] the lengths will show [1,2,3,2,3,2]
    lengths = [len(strings) for strings in arr]
    
    # Step 2: Count the frequency of each length using Counter. So the length_count will show [1:1 2:3 3:2]
    length_counts = Counter(lengths)
    
    # Step 3: Find the maximum frequency for here is 3 beacuse the 2 appear 3 times. And default is equal 0 use for the lenght_count is empty
    max_frequency = max(length_counts.values(), default=0)
    
    # Step 4: Identify the most frequent lengths in this case it is 2 becasue it will count the most_frequent lenghts base on max_frequency.
    most_frequent_lengths = [length for length, count in length_counts.items() if count == max_frequency]
    
    # Step 5: Return strings that have the most frequent lengths.
    result = [strings for strings in arr if len(strings) in most_frequent_lengths]
    
    return result

# result = most_tring_lengths_frequency(arr)
# print(result)
### Unit test function
def test_most_tring_lengths_frequency():
    assert most_tring_lengths_frequency(['a', 'ab', 'abc', 'cd', 'def', 'gh']) == ['ab', 'cd', 'gh']
    assert most_tring_lengths_frequency(['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'cc']) == ['aa', 'bb', 'cc']  
    assert most_tring_lengths_frequency(['hello', 'world', 'hi', 'bye']) == ['hello', 'world']
    assert most_tring_lengths_frequency(['a', 'b', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert most_tring_lengths_frequency([]) == []  # Empty array
    
# Run the unit test
test_most_tring_lengths_frequency()

