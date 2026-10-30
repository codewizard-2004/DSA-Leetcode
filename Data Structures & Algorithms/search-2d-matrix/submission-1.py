class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def binSearch(arr, tar):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if tar > arr[mid]:
                    l = mid + 1
                elif tar < arr[mid]:
                    r = mid - 1
                else:
                    return True
            return False

        up = 0
        down = ROWS - 1
        mid = 0

        while up <= down:
            mid = (up + down) // 2
            if target > matrix[mid][COLS - 1]:
                up += 1
            elif target < matrix[mid][0]:
                down -= 1
            else:
                break
        return binSearch(matrix[mid], target)
        