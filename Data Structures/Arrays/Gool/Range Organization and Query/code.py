from sortedcontainers import SortedList
class ManageRanges:
    def __init__(self):
        """"""
        self.ranges = SortedList()
    def add(self, start_point, end_point):
        """"""
        self.ranges.add((start_point, end_point))
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
