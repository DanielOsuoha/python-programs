from sortedcontainers import SortedList
class ManageRanges:
    def __init__(self):
        """"""
        self.ranges = SortedList()
    def add(start_point, end_point):
        """"""
        self.ranges.add((start_point, end_point))
    def find_point(point):
        # Binary search
        
