class sudoku:
    def __init__(self):
        self.size = 9
        self.subgrid_size = 3

    def _is_valid_cell(self, row: int, col: int) -> bool:
        """检查坐标是否有效"""
        return 0 <= row < self.size and 0 <= col < self.size

    def _get_subgrid_range(self, row: int, col: int) -> tuple:
        """获取指定位置所在的3x3子网格的范围"""
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size
        return (start_row, start_col)

    def _get_used_numbers(self, grid: list[list[int]], row: int, col: int) -> set:
        """
        获取指定位置所在行、列和子网格中已使用的数字
        返回: 已使用数字的集合
        """
        used = set()

        # 检查行
        used.update(num for num in grid[row] if num != 0)

        # 检查列
        used.update(grid[r][col] for r in range(self.size) if grid[r][col] != 0)

        # 检查3x3子网格
        start_row, start_col = self._get_subgrid_range(row, col)
        for r in range(start_row, start_row + self.subgrid_size):
            for c in range(start_col, start_col + self.subgrid_size):
                if grid[r][c] != 0:
                    used.add(grid[r][c])

        return used

    def lastRemainingCellInference(
        self, grid: list[list[int]]
    ) -> list[list[list[int]]]:
        """
        应用最后剩余格策略推断候选数
        先通过PN获取候选数集，如果有能确定的数(候选数集长度为1)，
        则将该位置集合内只有该数，否则为PN获取的候选数集
        返回: 每个位置的候选数列表(3D数组)
        """
        # 首先获取所有位置的候选数
        candidates = self.possibleNumberInference(grid)

        # 创建一个新的候选数矩阵用于存储结果
        result = [[[] for _ in range(self.size)] for _ in range(self.size)]

        for num in range(1, 10):
            # 检查每一行
            for row in range(self.size):
                possible_cols = [
                    col
                    for col in range(self.size)
                    if grid[row][col] == 0 and num in candidates[row][col]
                ]
                if len(possible_cols) == 1:
                    col = possible_cols[0]
                    result[row][col] = [num]

            # 检查每一列
            for col in range(self.size):
                possible_rows = [
                    row
                    for row in range(self.size)
                    if grid[row][col] == 0 and num in candidates[row][col]
                ]
                if len(possible_rows) == 1:
                    row = possible_rows[0]
                    result[row][col] = [num]

            # 检查每个3x3子网格
            for sg_row in range(0, self.size, self.subgrid_size):
                for sg_col in range(0, self.size, self.subgrid_size):
                    possible_cells = []
                    for r in range(sg_row, sg_row + self.subgrid_size):
                        for c in range(sg_col, sg_col + self.subgrid_size):
                            if grid[r][c] == 0 and num in candidates[r][c]:
                                possible_cells.append((r, c))
                    if len(possible_cells) == 1:
                        r, c = possible_cells[0]
                        result[r][c] = [num]

        # 合并结果：如果LRC找到了确定数字则使用，否则保留PN的候选数
        for row in range(self.size):
            for col in range(self.size):
                if grid[row][col] == 0:
                    if result[row][col]:  # LRC找到了确定数字
                        pass  # 保留LRC的结果
                    else:
                        result[row][col] = candidates[row][col]  # 使用PN的候选数
        return result

    def possibleNumberInference(self, grid: list[list[int]]) -> list[list[list[int]]]:
        """
        应用候选数策略推断每个位置可能的数字
        返回: 每个位置的候选数列表(3D数组)
        """
        candidates = [[[] for _ in range(self.size)] for _ in range(self.size)]

        for row in range(self.size):
            for col in range(self.size):
                if grid[row][col] == 0:
                    used_numbers = self._get_used_numbers(grid, row, col)
                    possible = [num for num in range(1, 10) if num not in used_numbers]
                    candidates[row][col] = possible
        return candidates


sudoku_ins = sudoku()
