class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Init vars
        result = []
        curr_max = float("-inf")
        right = k

        # Starting window
        for i in range(k):
            if nums[i] > curr_max:
                curr_max = nums[i]

        result.append(curr_max)

        # Slide window to the right until we hit the end
        # Keep track of the numbers entering on the right & leaving on left
        while right < len(nums):
            left = right - k + 1

            leaving = nums[left - 1]
            entering = nums[right]

            print(
                f"left index: {left}\n"
                + f"right index: {right}\n"
                + f"window: {nums[left:right+1]}\n"
                + f"exiting window: {leaving}\n"
                + f"entering window: {entering}\n"
            )

            # If entering > curr_max, set curr_max to num entering
            if entering > curr_max:
                curr_max = entering
            
            # If leaving == curr_max, scan for the max
            if leaving == curr_max:
                # Default to first num in window
                curr_max = nums[left]

                for i in range(left, right + 1):
                    if nums[i] > curr_max:
                        curr_max = nums[i]

            # If entering is not bigger than max, and we
            # aren't losing max, we already know the max in the window
            right += 1
            result.append(curr_max)

        return result
