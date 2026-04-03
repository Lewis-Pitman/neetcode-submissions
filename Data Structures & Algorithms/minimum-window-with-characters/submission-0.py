from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Init vars
        best_indices = (0, 0)
        best_length = float("inf")
        s_size = len(s)
        t_size = len(t)

        left, right = 0, 0

        # Init dicts
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        # Init dict of t char occurrences
        for char in t:
            t_dict[char] += 1

        # Start with the first character in the dict
        s_dict[s[0]] += 1

        # Main loop
        while right < s_size:
            # Check to see if all t chars are present in window
            all_t_chars_present = True
            for key in t_dict.keys():
                if s_dict[key] < t_dict[key]:
                    all_t_chars_present = False
                    break

            window_smaller_than_current_best = lambda: right - left < best_length
            
            if all_t_chars_present:
                if window_smaller_than_current_best():
                    best_length = right - left
                    best_indices = (left, right)

                # Move left pointer up
                s_dict[s[left]] -= 1
                left += 1
            else:
                # Move right pointer up
                right += 1
                if right < s_size:
                    s_dict[s[right]] += 1

        if best_length == float("inf"):
            return ""
        else:
            return s[best_indices[0]:best_indices[1] + 1]