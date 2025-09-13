# 18th August 2025
# leetcode-link -->https://leetcode.com/problems/course-schedule/description/

# Main Concept : 
# calculate the indegrees of each node 
# add nodes to 
#               

# Intuition:

from typing import List
from collections import deque

class Solution:

    # Kahn's Algorithm -> Topological Sort using BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = [[] for i  in range(numCourses)]        
        for source , destination in prerequisites:
            indegree[destination] += 1
            adjList[source].append(destination)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        finish = 0 
        
        while q:
            node = q.popleft()
            finish += 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
    
        
                

        
        
        

