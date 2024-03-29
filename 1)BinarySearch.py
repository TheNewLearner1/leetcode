def binarySearch(nums, target):
    (left, right) = (0, len(nums) - 1)
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
if __name__ == '__main__':
    nums = list(range(1, 100))
    target = 5
    index = binarySearch(nums, target)
    if index != -1:
        print(index)
    else:
        print('not-found')