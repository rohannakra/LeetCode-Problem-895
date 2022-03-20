# https://leetcode.com/problems/maximum-frequency-stack/

import numpy as np

class FreqStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:    # Basically append method.
        self.stack.append(val)

    def pop(self) -> int:    # Pop method, but pops the most frequent element.
        mock_stack = self.stack[:]
        unique_nums = []

        while True:
            if len(mock_stack) == len(np.unique(np.array(mock_stack)).tolist()):
                mock_stack = [mock_stack[-1]]    # Just remove last item if all items are unique.
                break

            elif len(mock_stack) != 1:    # Go through each item and remove the ones that are unique
                for num in mock_stack:
                    if num not in unique_nums:
                        mock_stack.remove(num)
                        unique_nums.append(num)

                unique_nums.clear()

            else: break

        most_freq_num = mock_stack[0]         
        reversed_stack = self.stack[::-1]

        reversed_stack.remove(most_freq_num)    # the number that is most frequent... the closest to the end is removed

        self.stack = reversed_stack[::-1]    # After removing most freqent item, update stack.

        return most_freq_num

freq_stack = FreqStack()

freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(4)
freq_stack.push(5) # The stack is [5,7,5,7,4,5]
freq_stack.pop()   # 5 is the most frequent. The stack becomes [5,7,5,7,4].
freq_stack.pop()   # 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freq_stack.pop()   # 5 is the most frequent. The stack becomes [5,7,4].
freq_stack.pop()   # 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

print(freq_stack.stack)    # -> [5, 7]
