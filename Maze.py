class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m = len(maze[0])
        n = len(maze)
        
        been_there = [[0] * m ]*n
        pos = ball
        while been_there[pos[0]][pos[1]] != 1:
            been_there[pos[0]][pos[1]] = 1
            if ball[0] > maze[0]:
                