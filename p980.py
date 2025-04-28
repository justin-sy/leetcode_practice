class Solution:
    def __init__(self):
        self.total = 0
    
    def check(self,g):
        for x in g:
            for y in x:
                if y != -1:
                    return False
        return True
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(cur,x,y):    
            cur[x][y] = -1
            if grid[x][y] == 2:
                if self.check(cur):
                    self.total +=1
                return
            if x-1 >= 0 and cur[x-1][y] != -1:
                backtrack([i[:] for i in cur],x-1,y)
            if y-1 >= 0 and cur[x][y-1] != -1:
                backtrack([i[:] for i in cur],x,y-1)
            if x+1 < len(grid) and cur[x+1][y] != -1:
                backtrack([i[:] for i in cur],x+1,y)
            if y+1<len(grid[0]) and cur[x][y+1] != -1:
                backtrack([i[:] for i in cur],x,y+1)
            return
        x = 0
        y = 0
        for i in range(len(grid)):
            for z in range(len(grid[0])):
                if grid[i][z] == 1:
                    x,y=i,z
                    break
        backtrack([i[:] for i in grid],x,y)
        return self.total