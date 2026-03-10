"""
八皇后问题单元测试
使用pytest框架，验证求解器的正确性
作者：借助Cursor AI协作完成
"""
import sys
import os

# 解决导入路径问题：把hw01目录加入Python搜索路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.queen import solve_n_queens

def test_8_queens_solution_count():
    """测试8皇后问题的解数量是否为92"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92

def test_solution_validity():
    """测试解的合法性：无同行/同列/同斜线"""
    solutions = solve_n_queens(8)
    for sol in solutions:
        # 检查列唯一性
        assert len(sol) == len(set(sol))
        # 检查斜线唯一性
        diag1 = [col - row for row, col in enumerate(sol)]
        diag2 = [col + row for row, col in enumerate(sol)]
        assert len(diag1) == len(set(diag1))
        assert len(diag2) == len(set(diag2))

def test_boundary_case_n1():
    """测试边界情况：n=1时返回1个解"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert solutions[0] == [0]

def test_boundary_case_n2():
    """测试边界情况：n=2时无解"""
    solutions = solve_n_queens(2)
    assert len(solutions) == 0