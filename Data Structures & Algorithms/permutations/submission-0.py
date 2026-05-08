class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        num_len = len(nums)

        def backtrack(curr_ls: list[int], curr_chosen: list[bool]) -> None:
            if len(curr_ls) >= num_len:
                result.append(curr_ls.copy())
                return

            for index, chosen in enumerate(curr_chosen):
                if not chosen:
                    # Choose current index
                    curr_chosen[index] = True
                    curr_ls.append(nums[index])
                    backtrack(curr_ls, curr_chosen)

                    # Undo
                    curr_ls.pop()
                    curr_chosen[index] = False

        backtrack([], [False] * len(nums))
        
        return result