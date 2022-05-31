class Maze:
    def __init__(self, size):
        self.maze_size = size
        self.new_maze = []
        self.start_x = -1
        self.start_y = -1
        self.finish_x = 0
        self.finish_y = 0
        self.create_maze()

    def create_maze(self):
        for row in range(self.maze_size):
            self.new_maze.append([])
            for column in range(self.maze_size):
                self.new_maze[row].append([" "])

    def check_step(self, step):
        check_x = self.start_x
        check_y = self.start_y
        position = [[check_x, check_y]]
        for char in step:
            if char == "D":
                check_x += 1
                check_y = check_y
            elif char == "U":
                check_x -= 1
                check_y = check_y
            elif char == "R":
                check_x = check_x
                check_y += 1
            elif char == "L":
                check_x = check_x
                check_y -= 1

            if [check_x, check_y] in position:
                return False, None, None
            else:
                position.append([check_x, check_y])

        try:
            value = self.new_maze[check_x][check_y]
        except IndexError:
            return False, None, None
        if value != "X":
            return True, check_x, check_y
        elif value == "X":
            return False, None, None

    def print_maze(self, way):
        check_x = self.start_x
        check_y = self.start_y
        for char in way[:-1]:
            if char == "D":
                check_x += 1
                check_y = check_y
            elif char == "U":
                check_x -= 1
                check_y = check_y
            elif char == "R":
                check_x = check_x
                check_y += 1
            elif char == "L":
                check_x = check_x
                check_y -= 1
            self.new_maze[check_x][check_y] = "o"

