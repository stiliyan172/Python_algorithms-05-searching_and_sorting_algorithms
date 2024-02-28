# linear search
def linear_search(target, nums):
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return "Not present"


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
print(linear_search(target, nums))


