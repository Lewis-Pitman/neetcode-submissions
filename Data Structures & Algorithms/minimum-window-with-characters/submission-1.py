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
        # We check s_size to avoid errors on empty/edge strings
        if s_size > 0:
            s_dict[s[0]] += 1
            if s[0] in t_dict and s_dict[s[0]] == t_dict[s[0]]:
                have = 1
            else:
                have = 0
        else:
            return ""

        # Keep track of how many character counts match in the current window, 
        # and how many we need to have all t chars matching in s
        need = len(t_dict)

        # Main loop
        while right < s_size:
            all_t_chars_present = lambda: need == have
            window_smaller_than_current_best = lambda: (right - left + 1) < best_length

            if all_t_chars_present():
                if window_smaller_than_current_best():
                    best_length = right - left + 1
                    best_indices = (left, right)

                # Check if removing this char from window results in losing a matching char
                # Decrement have ONLY if the count drops below the required amount
                if s[left] in t_dict and s_dict[s[left]] == t_dict[s[left]]:
                    have -= 1
                
                s_dict[s[left]] -= 1

                # Move left pointer up
                left += 1
            else:
                # Move right pointer up
                right += 1

                if right < s_size:
                    s_dict[s[right]] += 1
                    
                    # Check if adding this char from window results in gaining a matching char
                    # Increment have ONLY if the count exactly matches the requirement
                    if s[right] in t_dict and s_dict[s[right]] == t_dict[s[right]]:
                        have += 1

        if best_length == float("inf"):
            return ""
        else:
            return s[best_indices[0]:best_indices[1] + 1]