# Python程序设计 第二次作业 第3题
# 文件名：homework2_3.py
# 题目：使用BFS寻找迷宫最短步数（50分）
# 只需补全bfs函数中的TODO。


def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    # visited记录是否已加入过搜索列表；整个搜索过程共用，不随换层清空。
    visited = [[False] * cols for _ in range(rows)]
    start_row, start_col = start
    # 起点从一开始就在搜索列表中，先标记，避免被再次加入。
    visited[start_row][start_col] = True

    # queue保存当前这一层的位置；同一层到起点的最短距离相同。
    queue = [start]
    steps = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        # 每处理新的一层，都创建一个空列表收集下一层的位置。
        next_queue = []

        for row, col in queue:
            # TODO 1: 如果当前位置就是终点，返回steps
            if (row, col) == end:
                return steps
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # TODO 2: 判断相邻位置是否在边界内
                if 0 <= new_row < rows and 0 <= new_col < cols:
                # TODO 3: 在边界内，再判断是否为通路且尚未访问
                    if maze[new_row][new_col] == 0 and not visited[new_row][new_col]:
                # TODO 4: 对满足条件的位置，标记为已访问
                        visited[new_row][new_col] = True
                # TODO 5: 将坐标(new_row, new_col)加入next_queue
                        next_queue.append((new_row, new_col))
                pass

        # 当前层全部检查完，再切换到下一层，步数增加1。
        queue = next_queue
        steps += 1

    # TODO 6: 所有层处理完仍未到达终点，返回-1
    return -1


maze = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
]
start = (0, 0)
end = (9, 9)
# 以下调用、输出和检查代码已经提供，请保留，不需要修改。
def show_result(name, maze, start, end, expected):
    result = bfs(maze, start, end)
    print(f"测试：{name}")
    if type(result) is not int:
        print("结果：请让bfs返回整数步数，无路可达时返回-1")
    elif result == -1:
        print("结果：无路可达")
    else:
        print(f"最短步数：{result}")
    passed = type(result) is int and result == expected
    print(f"测试结果：{'通过' if passed else '未通过'}")
    print()
    return passed


passed_count = 0
if show_result("原始迷宫", maze, start, end, 18):
    passed_count += 1
if show_result("起终点相同", maze, start, start, 0):
    passed_count += 1

# 逐行复制，修改检查场景时不影响原始迷宫。
blocked_maze = [row.copy() for row in maze]
blocked_maze[0][1] = 1
blocked_maze[1][0] = 1
if show_result("起点被围住", blocked_maze, start, end, -1):
    passed_count += 1

print(f"通过测试：{passed_count}/3")