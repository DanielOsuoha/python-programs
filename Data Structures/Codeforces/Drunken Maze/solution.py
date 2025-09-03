class Solution:
    def find_shortest_path(matrix, start, end):
        from collections import deque
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        queue = deque([start])
        seen = {start} 
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r,c) == end:
                    return count 
                for x, y in directions:
                    dx, dy = r+x, c+y
                    if (dx, dy) not in seen:
                        queue.append((dx, dy))



if __name__ == 'main':
    #get input
    import sys
    read = sys.stdin.readline
    # write = sys.stdout.write
    M, N = map(int, read().split())
    matrix = []
    ans = 0
    for _ in range(M):
        matrix.append(read().split())
    solution = Solution()
    print(solution.find_shortest_path(matrix, start, end))