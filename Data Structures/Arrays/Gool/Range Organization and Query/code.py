from sortedcontainers import SortedList
class ManageRanges:
    def __init__(self):
        """"""
        self.ranges = SortedList()
    def add(self, start_point, end_point):
        """"""
        left_idx = self._find_leftmost_overlap(start_point, end_point)
        right_idx = self._find_rightmost_overlap(start_point, end_point)
        if left_idx <= right_idx:
            merged_start = min(start_point, self.ranges[left_idx][0])
            merged_end = max(end_point, self.ranges[right_idx][-1])
            del self.ranges[left_idx:right_idx+1]
            self.ranges.add((merged_start, merged_end))
        else:
            self.ranges.add((start_point, end_point))
    
    def _find_leftmost_overlap(self, start, end):
        left, right = 0, len(self.ranges)-1
        while left < right:
            mid = (left + right) // 2
            if self.ranges[mid][1] >= start:
                right = mid 
            else:
                left = mid + 1
            
            if left < len(self.ranges) and self.ranges[left][0] <= end:
                return left
            return len(self.ranges)

    def _find_rightmost_overlap(self, start, end):
        left, right = 0, len(self.ranges)-1
        result = -1
        while left < right:
            mid = (left + right) // 2
            if self.ranges[mid][0] <= end:
                left = mid 
                result = mid + 1
            else:
                right = mid 
            
            if result >= 0 and self.ranges[result][1] >= start:
                return result
            return -1

    def find_point(self, point):
        """"""
        left, right = 0, len(self.ranges)
        while left < right:
            mid = (left + right) // 2
            start, end = self.ranges[mid]
            if start <= point <= end:
                return True
            elif point < start:
                right = mid 
            else:
                left = mid + 1
        return False
