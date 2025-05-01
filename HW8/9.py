def most_common(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    max_count = max(count.values())  
    most_frequent_numbers = [num for num, freq in count.items() if freq == max_count]
    
    return most_frequent_numbers
