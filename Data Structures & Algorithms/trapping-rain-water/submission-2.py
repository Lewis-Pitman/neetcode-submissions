class Solution:
    def trap(self, height: List[int]) -> int:
        def scan(height_list):
            result = 0
            i = 0
            # Your original logic here
            while i < len(height_list) and height_list[i] == 0:
                i += 1
            
            k = i + 1
            while k < len(height_list):
                obstructions = 0
                # Search for a wall >= current wall
                while k < len(height_list) and height_list[k] < height_list[i]:
                    # We skip the return result here because we want to 
                    # find the tallest wall if a >= one doesn't exist
                    obstructions += height_list[k]
                    k += 1
                
                # If we found a wall >= height[i]
                if k < len(height_list):
                    water = (min(height_list[i], height_list[k]) * (k - i - 1)) - obstructions
                    result += water
                    i = k
                    k = i + 1
                else:
                    # No more walls >= height[i] exist. 
                    # We stop and let the reverse scan handle this section.
                    break
            return result, i

        # 1. Scan Left to Right
        forward_water, stop_index = scan(height)
        
        # 2. Scan Right to Left (only up to the tallest peak found in pass 1)
        # This uses your SAME logic on the reversed remaining part
        backward_water, _ = scan(height[stop_index:][::-1])
        
        return forward_water + backward_water