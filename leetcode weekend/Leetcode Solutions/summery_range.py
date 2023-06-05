
def summaryRanges(self, nums: List[int]) -> List[str]:
    if len(nums) == 1:
        return [str(nums[0])]
    ranges = []
    start, running = None, None
    for index, num in enumerate(nums):
        if start is None:
            start, running = num, num
            continue
        if running is not None:
            if running + 1 == num:
                running = num
            else:
                ranges.append(str(start) if start == running else f"{str(start)}->{running}")
                start, running = num, num
        if index == len(nums) - 1:
            ranges.append(str(start) if start == running else f"{str(start)}->{running}")
            start, running = num, num

    return ranges