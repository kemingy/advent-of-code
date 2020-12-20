from utils import get_input


def two_sum(nums, target=2020):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left <= right:
        s = nums[left] + nums[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return nums[left], nums[right]
    return None, None


def three_sum(nums, target=2020):
    nums.sort()
    n = len(nums)
    for i in range(n-2):
        left, right = i + 1, n - 1
        t = target - nums[i]
        while left <= right:
            s = nums[left] + nums[right]
            if s < t:
                left += 1
            elif s > t:
                right -= 1
            else:
                return nums[i], nums[left], nums[right]

    return None, None, None


if __name__ == "__main__":
    nums = [int(x) for x in get_input()]
    x, y = two_sum(nums)
    if x is not None:
        print(f"{x} x {y} = {x * y}")

    x, y, z = three_sum(nums)
    if x is not None:
        print(f"{x} x {y} x {z} = {x * y * z}")
