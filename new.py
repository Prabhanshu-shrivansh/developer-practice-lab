print("Jay")
def find_missing(nums):
    n = len(nums) + 1
    expected = n * (n + 1) // 2
    actual = 0

    for i in nums:
        actual += i

    return expected - actual


nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print(find_missing(nums))