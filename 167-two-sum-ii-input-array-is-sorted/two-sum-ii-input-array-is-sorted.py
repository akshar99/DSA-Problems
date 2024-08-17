class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =  0
        right = len(numbers) - 1
        sums = 0
        while left < right:
            current_sum = numbers[left] + numbers[right]
            print(current_sum)
            if current_sum == target:
                return[left +1, right +1]

            elif current_sum < target:
                left +=1

            else:
                right -= 1
        return []