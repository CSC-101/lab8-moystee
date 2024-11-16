def groups_of_3(nums: list[int]) -> list[list[int]]:
    grouped = []
    group = []
    for i in range(len(nums)):
        group.append(nums[i])
        if len(group) == 3:
            grouped.append(group)
            group = []
    if group:
        grouped.append(group)
    return grouped
