# __contains__() 메서드를 구현한 객체, 일반적으로 Boolean값을 반환하도록 구현
# 해당 키워드는 in 키워드가 발견될 때 호출됨.



#x, y를 멤버변수로 갖고 있는 coord가 그리드의 영역에 있는지 검사하고 표시하고 싶을 때, 일반적인 구현
# less Pythonic
def mark_coordinate(grid, coord):
    if 0 <= coord.x < grid.width and 0 <= coord.y < grid.height:
        grid[coord] = MARKED


# more Pythonic
class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.hegiht = height
        self.limit = Boundaries(width, height) # 의도를 직관적으로 설명하였음.

    def __contains__():
        return coord in self.limits

# Usage
def mark_coordinate(grid, coord):
    if coord in grid:  #  in절을 통해 직관적으로 Grid 안에 있는지 체크하는 듯한 느낌을 받을 수 있음.
        grid[coord] = MARKED 