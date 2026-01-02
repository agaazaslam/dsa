


#### Date: 31st December 2025

## Search a 2D Matrix

### Problem Link
- https://leetcode.com/problems/search-a-2d-matrix/description/ 

### Intuition
- Binary search works only on a **sorted array**
- At every step, compare the **middle element** with the target
- If the middle element equals the target, return its index
- If the target is smaller, discard the **right half**
- If the target is larger, discard the **left half**
- Repeat until the element is found or the search space becomes empty
- **Important** → Use `mid = left + (right - left) // 2` to safely calculate the middle index

---

### Complexity Analysis
- **Time Complexity:** `O(log n)`  
  The search space is reduced by half in each iteration
- **Space Complexity:** `O(1)`  
  Only constant extra space is used

---

### Key Insight
> Because the array is sorted, one comparison is enough to eliminate half of the remaining elements.

