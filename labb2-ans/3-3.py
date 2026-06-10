def pair_sums(nums, sum):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == sum:
                pairs.append((nums[i], nums[j]))

    return pairs


the_list = [6, 6, 7, 1, 10, 2, 5, 8, 9, 3, 14, 67]

print(pair_sums(the_list, 12))
