# def quick_sort(start, end, nums):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         if nums[left] > nums[pivot] > nums[right]:
#             nums[left], nums[right] = nums[right], nums[left]
#
#         if nums[left] <= nums[pivot]:
#             left += 1
#
#         if nums[right] >= nums[pivot]:
#             right -= 1
#
#     nums[pivot], nums[right] = nums[right], nums[pivot]
#     quick_sort(start, right - 1, nums)
#     quick_sort(left, end, nums)
#
# nums = [int(x) for x in input().split()]
#
# quick_sort(0, len(nums) - 1, nums)
#
# print(*nums)

def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


print(quicksort([2, 3, 4, 1, 9, 3, 4, 2, 6, 0]))