from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def islegal(i: int, j:int) -> bool:
            nonlocal m, n
            return 0<=i<m and 0<=j<n

        def getnext(i:int, j:int) -> list:
            neighbors = [(i+1,j), (i, j+1), (i+1, j+1)]
            print(f"{i=},{j=},{neighbors=}")
            legal_neighbors = list(filter(lambda t:islegal(t[0],t[1]), neighbors))
            print(f'{legal_neighbors=}')
            return legal_neighbors
        
        def getNonVisited(l: list) -> list:
            nonlocal visited
            nonvisited = list(filter(lambda x,y: visited[x][y], l))
            return nonvisited
        
        def getzeronext(l: list) -> list:
            nonlocal grid
            zeronext = list(filter(lambda x,y: grid[x][y]==0, l))
            return zeronext

        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        i, j=0,0
        if grid[i][j]==1:
            return float('inf')
        
        path = [(0,0)]
        length = float('inf')
        queue = deque([(0,0,0)])
        while queue:
            fi, fj, d = queue.popleft()
            if fi==m-1 and fj==n-1:
                length = min(length, d)
            visited[fi][fj]=True
            nextnodes = getnext(fi, fj)

            nextnonvisited = getNonVisited(nextnodes)
            nextzeroes = getzeronext(nextnonvisited)
            
            print(f'{nextnodes=}, {nextnonvisited=}, {nextzeroes=}')
            nexts = [(x,y,d+1) for x,y in nextzeroes]
            print(f'{nexts=}')
            queue.extend(nexts)
        
        return length

s = Solution()
input = [[0,1],[1,0]]
pathlen = s.shortestPathBinaryMatrix(input)
print(pathlen)