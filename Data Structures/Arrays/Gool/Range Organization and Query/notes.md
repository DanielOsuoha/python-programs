## Problem: Range Containment Query

### Description
Design a data structure that stores a set of **non-overlapping numeric ranges** and efficiently determines whether a given point lies within **any** of the stored ranges.

Your class should support the following operations:

1. **add_range(start, end)** – Add a closed interval `[start, end]` (inclusive) to the structure.  
   - You may assume that `start <= end`.
   - If the new range overlaps or touches existing ranges, they should be merged into one.

2. **query(point)** – Return `True` if `point` lies within any existing range, otherwise return `False`.

---

### Example

```python
ranges = RangeModule()
ranges.add_range(5, 10)
ranges.add_range(15, 20)
ranges.add_range(10, 15)   # merged automatically into [5, 20]

print(ranges.query(7))     # True  (in [5, 20])
print(ranges.query(14))    # True  (in [5, 20])
print(ranges.query(25))    # False


Constraints

-10^9 <= start, end, point <= 10^9

Up to 10^5 operations.

Expected time complexity:

add_range: O(log n) (using balanced search tree or bisect)

query: O(log n)