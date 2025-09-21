# Longest Increasing/Non-Decreasing Subsequence (LIS/LNDS) via Patience Sorting

### Problem Pattern
- When asked for:
  - *Longest increasing/non-decreasing subsequence (LIS/LNDS)*
  - *Minimum removals/merges to make an array sorted*
  - *Partitioning into non-decreasing subsequences*
- Use this **patience sorting + binary search** trick.

---

### Key Idea
- Maintain an array `piles` where each element = the smallest possible tail of a subsequence of a given length.  
- For each number `x`:
  - Find position `idx = bisect_right(piles, x)`  
    - If `idx == len(piles)`: append (extend subsequence).  
    - Else: replace `piles[idx] = x` (keep tails minimal).
- At the end, `len(piles)` = length of LIS/LNDS.  
- If problem asks for *minimum deletions/merges*, 


---

### Python Template
```python
from typing import List
import bisect

def lnds_length(nums: List[int]) -> int:
  piles = []
  for x in nums:
      idx = bisect.bisect_right(piles, x)  # use bisect_left for strictly increasing
      if idx == len(piles):
          piles.append(x)
      else:
          piles[idx] = x
  return len(piles)


