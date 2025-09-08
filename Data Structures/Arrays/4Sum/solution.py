class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import defaultdict, Counter
        sum_map = defaultdict(int)
        n = len(nums1)
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        counter3 = Counter(nums3)
        counter4 = Counter(nums4)
        
        for n1, freq1 in counter1.items():
            for n2, freq2 in counter2.items():
                val = n1 + n2
                sum_map[val] += freq1 * freq2 
        
        count = 0
        for n3, freq3 in counter3.items():
            for n4, freq4 in counter4.items():
                val = n3 + n4
                if -val in sum_map:
                    count += sum_map[-val] * freq3 * freq4
        return count
        
if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    soln = Solution()
    print(soln.fourSumCount(nums1, nums2, nums3, nums4))