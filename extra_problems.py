from typing import List, Dict

from linked_list_node import LinkedListNode


class ExtraProblems:
    def problem1(self, root_nodes: List[LinkedListNode]) -> LinkedListNode:
        # You are given an array of k linked-lists lists, each linked-list is
        # sorted in ascending order. Merge all the linked-lists into one sorted
        # linked-list and return it.
        
        # Complexity: O ( n ^ 2 ) at worst where n is the total amount of nodes.
        sorted_root = LinkedListNode()
        valid_nodes = [n for n in root_nodes if n is not None]
        
        while len(valid_nodes) != 0:
            # add min_value to new LL
            nodes_data = [n.data for n in valid_nodes]
            min_value = min(nodes_data)  #
            sorted_root.insert(min_value)
            
            # advance the minimum node only
            idx = nodes_data.index(min_value)
            valid_nodes[idx] = valid_nodes[idx].next
            
            valid_nodes = [n for n in valid_nodes if n is not None]
        return sorted_root

    def _get_next_island(self, _grid: List[List[int]]) -> List[int]:
        # returns empty list if none found
        for i in range(len(_grid)):
            for j in range(len(_grid[i])):
                if _grid[i][j] == 1:
                    return [i, j]
        return []

    def _fill_ones_rec(self, _grid: List[List[int]], i: int, j: int) -> None:
        vert_bound = len(_grid) - 1
        horiz_bound = len(_grid[0]) - 1
        
        _grid[i][j] = 0
        
        if i != 0 and _grid[i - 1][j]:  # top
            self._fill_ones_rec(_grid, i - 1, j)
            
        if i != vert_bound and _grid[i + 1][j]:  # bottom
            self._fill_ones_rec(_grid, i + 1, j)
        
        if j != 0 and _grid[i][j - 1]:  # left
            self._fill_ones_rec(_grid, i, j - 1)
        
        if j != horiz_bound and _grid[i][j + 1]:
            self._fill_ones_rec(_grid, i, j + 1)
    
    def problem2(self, grid: List[List[int]]) -> int:
        # Given an m x n 2D binary grid which represents a map of '1's
        # (land) and '0's (water), return the number of islands. An island is
        # surrounded by water and is formed by connecting adjacent lands
        # horizontally or vertically. You may assume all four edges of the grid
        # are all surrounded by water.
        island_count = 0
        island_coords = self._get_next_island(grid)
        while island_coords:
            # fill in islands in place
            self._fill_ones_rec(grid, island_coords[0], island_coords[1])
            island_count += 1
            
            # get new island
            island_coords = self._get_next_island(grid)
        return island_count

    def _fib_memo(self, curr: int, n: int, memo: Dict[int, int]) -> int:
        if curr in memo:
            return memo[curr]
        
        new_res = memo[curr - 1] + memo[curr - 2]
        memo[curr] = new_res
        
        if curr == n:
            return new_res
        return self._fib_memo(curr + 1, n, memo)
        
    def problem3(self, n: int) -> int:
        # Return the nth fibonacci number
        return self._fib_memo(3, n, {1: 0, 2: 1})
