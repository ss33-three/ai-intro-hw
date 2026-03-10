"""
八皇后问题求解器
使用回溯法枚举所有合法的皇后摆放位置，排除同行/同列/同斜线的情况
作者：借助Cursor AI协作完成
"""


def solve_n_queens(n: int = 8) -> list[list[int]]:
    """
    求解n皇后问题，返回所有合法解

    参数:
        n: 皇后数量（默认8）

    返回:
        所有合法解的列表，每个解是长度为n的列表，代表每行皇后所在的列号
    """
    solutions = []  # 存储所有合法解

    def backtrack(row: int, cols: set, diag1: set, diag2: set, path: list):
        """
        回溯递归函数
        row: 当前处理的行
        cols: 已占用的列集合
        diag1: 已占用的左上-右下斜线（col - row 为定值）
        diag2: 已占用的右上-左下斜线（col + row 为定值）
        path: 当前行的皇后列号
        """
        # 递归终止条件：所有行都放置了皇后
        if row == n:
            solutions.append(path.copy())
            return

        # 遍历当前行的所有列
        for col in range(n):
            # 剪枝：排除同列、同斜线的情况
            if col not in cols and (col - row) not in diag1 and (col + row) not in diag2:
                # 选择当前列
                cols.add(col)
                diag1.add(col - row)
                diag2.add(col + row)
                path.append(col)

                # 递归处理下一行
                backtrack(row + 1, cols, diag1, diag2, path)

                # 回溯：撤销选择
                path.pop()
                diag2.remove(col + row)
                diag1.remove(col - row)
                cols.remove(col)

    # 初始化参数，从第0行开始回溯
    backtrack(0, set(), set(), set(), [])
    return solutions


# 测试入口（可选）
if __name__ == "__main__":
    solutions = solve_n_queens(8)
    print(f"八皇后问题共有 {len(solutions)} 个合法解")
    # 打印前3个解示例
    for i, sol in enumerate(solutions[:3]):
        print(f"解{i + 1}: {sol}")