class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []

        curr_num = ""
        curr_str = ""

        for char in s:
            if char.isdigit():
                curr_num += char
                continue

            if char == "[":
                num_stack.append(int(curr_num))
                str_stack.append(curr_str)

                curr_str = ""
                curr_num = ""
                continue
            
            if char == "]":
                amount = num_stack.pop()
                s = str_stack.pop()

                curr_str = s + (curr_str * amount)
                continue

            # If char is regular letter:
            curr_str += char
        
        return curr_str
