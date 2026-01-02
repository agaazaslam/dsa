
#### Date: 2nd Jan 2026

##### Intuition
- use dict with sets to check uniqueness. 
- maintain three dicts with row , column and square uniqueness
- for square divide the index of row & column by 3 and store in dict as pairs (r//3 , c//3)

#### Date : 2nd Jan 2026

## Problem : Valid Sudoku

### Problem Link :
- https://leetcode.com/problems/valid-sudoku/description/

---

### Intuition
- Use sets to track seen numbers:
  - One set per row
  - One set per column
  - One set per 3×3 box
- While traversing the board:
  - If a number already exists in its row, column, or box → invalid
  - Otherwise, insert it into the corresponding sets
- use dict with sets to check uniqueness. 
- maintain three dicts with row , column and square uniqueness
- for square divide the index of row & column by 3 and store in dict as pairs (r//3 , c//3)

---

### Complexity Analysis
- **Time Complexity:** `O(n^2)`  
  The board size is fixed at `9 × 9`, so at most 81 cells are checked.
- **Space Complexity:** `O(n^2)`  

---

### Key Insight
> The problem is not about solving Sudoku, but about detecting duplicates under given constraints.  
> Sets allow instant duplicate checks, making validation straightforward and efficient.




