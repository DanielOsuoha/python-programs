class Solution:
    def kadane(array):
        cur_sum = 0
        max_sum = float('-inf')
        for number in array:
            cur_sum += number
            max_sum = max(max_sum, cur_sum)
            cur_sum = max(cur_sum, 0)
        return max_sum 
    

if __name__ == "main":
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    soln = Solution()
    print(soln.kadane(array))