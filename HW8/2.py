def average(nums):
    if not nums:
        return None
    return round(sum(nums) / len(nums), 1)
