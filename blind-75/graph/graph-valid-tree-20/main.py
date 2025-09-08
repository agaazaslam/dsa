

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n-1:
            return False

        tree = [[] for i in range(n)]
        visited = set()

        for u , v in edges:
            tree[u].append(v)
            tree[v].append(u)

        
        def dfs(node : int , parent : int ):

            if node in visited:
                return False
            
            visited.add(node)
            for nei in tree[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
                
            return True
        

        return dfs(0 , -1) and n == len(visited)   
