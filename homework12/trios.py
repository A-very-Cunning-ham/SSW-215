def findTrios(numSet, goal):
    def helper(nums, current_nums):

        if len(current_nums) == 3:
            if sum(current_nums) == goal:
                return [current_nums]
            else:
                return []

        if nums == []:
            return []

        if len(current_nums) > 3:
            return helper(nums[1:], [])
        return helper(nums[1:], current_nums + [nums[0]]) + helper(
            nums[1:], current_nums)

    trios = helper(numSet, [])

    if trios:
        print("Trio exists")
        print(f"The trio which contains the given sum are {trios}")
    else:
        print("Trio does not exist")

    return trios


if __name__ == '__main__':

    numSet = [3, 7, 4, 0, 9, 5, 1, 2]
    goal = 7

    findTrios(numSet, goal)
