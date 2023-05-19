def find_duplicate(nums):
    if (len(nums) <= 1):
        return False

    nums.sort()

    prev_num = nums[0]
    for num in nums[1:]:
        if not isinstance(num, int) or num <= 0:
            return False
        elif num == prev_num:
            return num
        prev_num = num
    return False
