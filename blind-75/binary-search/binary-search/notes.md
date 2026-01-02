
#### Date: 31st December 2025

### Intuition
- Binary search works only on a **sorted array**
- At every step, compare the **middle element** with the target
- If the middle element equals the target, return its index
- If the target is smaller, discard the **right half**
- If the target is larger, discard the **left half**
- Repeat until the element is found or the search space becomes empty
- **Important** → Use `mid = left + (right - left) // 2` to safely calculate the middle index

---

### Algorithm
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate `mid`
   - If `nums[mid] == target`, return `mid`
   - If `nums[mid] < target`, set `left = mid + 1`
   - Else, set `right = mid - 1`
3. If the loop ends, return `-1`

---

### Complexity Analysis
- **Time Complexity:** `O(log n)`  
  The search space is reduced by half in each iteration
- **Space Complexity:** `O(1)`  
  Only constant extra space is used

---

### Key Insight
> Because the array is sorted, one comparison is enough to eliminate half of the remaining elements.
