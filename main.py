from queue import Queue
import pygame
from maze import Maze
from tkinter import *
from tkinter import messagebox
Tk().withdraw()

CELL_SIZE = 30
WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE
MARGIN = 5
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
board_size = 10
window_size = [CELL_SIZE*board_size + (board_size+1)*MARGIN, CELL_SIZE*board_size + (board_size+1)*MARGIN]


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("BFS")


maze2 = Maze(board_size)


if __name__ == "__main__":
    program_end = False
    set_start_finish = True

    def find_path():
        for row in range(board_size):
            for column in range(board_size):
                if not (maze2.new_maze[row][column] == "S"
                        or maze2.new_maze[row][column] == "F"
                        or maze2.new_maze[row][column] == "X"):
                    maze2.new_maze[row][column] = " "
        queue = Queue()
        queue.put("")
        end_loop = False
        while not end_loop:
            old_path = queue.get()
            for next_step in ["D", "U", "R", "L"]:
                current_path = old_path + next_step
                valid_step, x_current_position, y_current_position = maze2.check_step(current_path)

                if valid_step:
                    queue.put(current_path)

                if x_current_position == maze2.finish_x and y_current_position == maze2.finish_y:
                    maze2.print_maze(current_path)
                    end_loop = True

            if queue.empty():
                messagebox.showinfo(title="BFS", message="No valid path")
                end_loop = True

    while not program_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_end = True
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if set_start_finish:
                        maze2.new_maze[maze2.start_x][maze2.start_y] = " "
                        maze2.new_maze[row][column] = "S"
                        maze2.start_x = row
                        maze2.start_y = column
                        set_start_finish = not set_start_finish

                    else:
                        if maze2.start_x != row or maze2.start_y != column:
                            maze2.new_maze[maze2.finish_x][maze2.finish_y] = " "
                            maze2.new_maze[row][column] = "F"
                            maze2.finish_x = row
                            maze2.finish_y = column
                            set_start_finish = not set_start_finish
                            find_path()

                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if maze2.new_maze[row][column] != "F" and maze2.new_maze[row][column] != "S":
                        if maze2.new_maze[row][column] == "X":
                            maze2.new_maze[row][column] = " "
                        else:
                            maze2.new_maze[row][column] = "X"

        for row in range(board_size):
            for column in range(board_size):
                if maze2.new_maze[row][column] == "X":
                    pygame.draw.rect(screen, GREY, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                elif maze2.new_maze[row][column] == "S":
                    pygame.draw.rect(screen, RED, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                elif maze2.new_maze[row][column] == "F":
                    pygame.draw.rect(screen, BLUE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                elif maze2.new_maze[row][column] == "o":
                    pygame.draw.rect(screen, GREEN, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                elif maze2.new_maze[row][column] != "X":
                    pygame.draw.rect(screen, WHITE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
        clock.tick(60)
        pygame.display.flip()
