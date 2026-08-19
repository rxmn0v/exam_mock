def rearrange_by_frequency(nums: list[int]) -> list[int]:
    numbers = {}

    for i in nums:
        soni = nums.count(i)
        numbers[i] = soni

    lst = []

    for num in numbers:
        for i in range(numbers[num]):
            lst.append(num)

    lst.sort(key=lambda x: lst.count(x))

    return lst


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4])) # [4, 4, 4, 5, 5, 3, 6]