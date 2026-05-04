class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()  # Stop duplicates

        def backtrack(curr_index, curr_path, curr_sum):
            # Base cases
            if curr_sum == target:
                result.append(curr_path.copy())
                return
            if curr_sum > target or curr_index >= len(candidates):
                return

            # Take current index
            curr_path.append(candidates[curr_index])
            backtrack(curr_index + 1, curr_path, curr_sum + candidates[curr_index])
            curr_path.pop()

            # Skip current index and handle duplicates by moving to the next different number
            next_index = curr_index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[curr_index]:
                next_index += 1

            backtrack(next_index, curr_path, curr_sum)

        backtrack(0, [], 0)
        return result