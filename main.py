from queue import Queue


def create_maze():
    new_maze = []
    new_maze.append(["X", "X", "X", "X", "X", "X", "X", "X", "X"])
    new_maze.append(["X", " ", " ", " ", " ", " ", "X", " ", "X"])
    new_maze.append(["X", " ", "X", " ", " ", "X", " ", " ", "S"])
    new_maze.append(["X", " ", "X", " ", " ", " ", " ", "X", "X"])
    new_maze.append(["X", " ", " ", "X", " ", "X", " ", " ", "X"])
    new_maze.append(["X", "X", " ", "X", " ", "X", " ", " ", "X"])
    new_maze.append(["X", "X", " ", "X", " ", "X", " ", "X", "X"])
    new_maze.append(["X", " ", " ", "X", " ", " ", " ", " ", "X"])
    new_maze.append(["X", "F", "X", "X", "X", "X", "X", "X", "X"])

    start_x = 0
    start_y = 0
    finish_x = 0
    finish_y = 0

    for y_cor, value in enumerate(new_maze):
        for x_cor, value2 in enumerate(value):
            if value2 == "S":
                start_x = x_cor
                start_y = y_cor
            elif value2 == "F":
                finish_x = x_cor
                finish_y = y_cor
    return new_maze, start_x, start_y, finish_x, finish_y


def check_step(st_x, st_y, step, maze_object):
    check_x = st_x
    check_y = st_y
    position = [(check_x, check_y)]
    for char in step:
        if char == "D":
            check_x = check_x
            check_y += 1
        elif char == "U":
            check_x = check_x
            check_y -= 1
        elif char == "R":
            check_x += 1
            check_y = check_y
        elif char == "L":
            check_x -= 1
            check_y = check_y

        if (check_x, check_y) in position:
            return False, None, None
        else:
            position.append((check_x, check_y))

    try:
        value = maze_object[check_y][check_x]
    except IndexError:
        return False, None, None
    if value != "X":
        return True, check_x, check_y
    elif value == "X":
        return False, None, None


def print_maze(maze_to_print, way, x, y):
    check_x = x
    check_y = y
    for char in way[:-1]:
        if char == "D":
            check_x = check_x
            check_y += 1
        elif char == "U":
            check_x = check_x
            check_y -= 1
        elif char == "R":
            check_x += 1
            check_y = check_y
        elif char == "L":
            check_x -= 1
            check_y = check_y
        maze_to_print[check_y][check_x] = "o"
    print(*maze_to_print, sep="\n")


maze, x_start, y_start, x_end, y_end = create_maze()

if __name__ == "__main__":

    queue = Queue()
    queue.put("")
    end_loop = False

    while not end_loop:
        old_path = queue.get()

        for next_step in ["D", "U", "R", "L"]:
            current_path = old_path + next_step
            valid_step, x_current_position, y_current_position = check_step(x_start, y_start, current_path, maze)

            if valid_step:
                queue.put(current_path)

            if x_current_position == x_end and y_current_position == y_end:
                print_maze(maze, current_path, x_start, y_start)
                end_loop = True

        if queue.empty():
            print("There is no valid way to exit point.")
            break
