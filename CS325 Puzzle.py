# Author: Serkan Bayramoglu
# Date: 24/05/2022
# Description:  This project uses BFS approach to find the shortest path from source coordinate (a,b) to destination
#               coordinate (x,y), of a 2D puzzle of size MxN that has N rows and M columns (N>=3 ; M>=3; M and N can be
#               different), moving only up, down, right or left by one empty cell. Each cell in the puzzle is either
#               empty or has a barrier. An empty cell is marked by ‘-’ and the one with a barrier is marked by ‘#’.

from queue import Queue


def solve_puzzle(Board, Source, Destination):
    """
    This function accepts an input of a MxN Board, Source coordinate and Destination coordinate, where cells of the
    Board is marked by '-' (empty cell) or '#' (barrier), and returns the minimum path from Source to Destination as
    a tuple consisting of a list of tuples showing the path, and a tuple consisting of a string showing the directions.
    """
    # construct an mxn matrix paths to store the tuples holding a list of tuples listing the path,
    # and a tuple showing directions
    y_len = len(Board)
    x_len = len(Board[0])
    paths = [[([], "") for i in range(x_len)] for j in range(y_len)]

    # initiate paths of the source cell
    paths[Source[0]][Source[1]][0].append(Source)

    # initiate simple queue, sq with enqueueing Source
    board_size = x_len * y_len
    sq = Queue(maxsize=board_size)
    sq.put(Source)

    while sq.qsize() > 0:
        # dequeue current data cd from sq
        cd = sq.get()

        # return the resulting path if the path has arrived to the Destination (if cd equals Destination)
        if (cd[0], cd[1]) == Destination:
            result = paths[Destination[0]][Destination[1]]
            return result

        # check above neighbor if exists
        if cd[0] > 0:
            # check if the neighbor cell is not visited, and has no barrier
            if len(paths[cd[0] - 1][cd[1]][0]) == 0 and Board[cd[0] - 1][cd[1]] == '-':
                # copy the path of the current cell to the neighbor, add the neighbor coordinates,
                # add "U" to the string, and enqueue the neighbor coordinates into sq
                temp_list = paths[cd[0]][cd[1]][0][:]
                temp_list.append((cd[0] - 1, cd[1]))
                temp_string = paths[cd[0]][cd[1]][1] + 'U'
                paths[cd[0] - 1][cd[1]] = (temp_list, temp_string)
                sq.put((cd[0] - 1, cd[1]))
        # check below neighbor if exists
        if cd[0] < y_len - 1:
            # check if the neighbor cell is not visited, and has no barrier
            if len(paths[cd[0] + 1][cd[1]][0]) == 0 and Board[cd[0] + 1][cd[1]] == '-':
                # copy the path of the current cell to the neighbour, add the neighbor coordinates,
                # add "D" to the string, and enqueue the neighbor coordinates into sq
                temp_list = paths[cd[0]][cd[1]][0][:]
                temp_list.append((cd[0] + 1, cd[1]))
                temp_string = paths[cd[0]][cd[1]][1] + 'D'
                paths[cd[0] + 1][cd[1]] = (temp_list, temp_string)
                sq.put((cd[0] + 1, cd[1]))
        # check right neighbor if exists
        if cd[1] < x_len - 1:
            # check if the neighbor cell is not visited, and has no barrier
            if len(paths[cd[0]][cd[1] + 1][0]) == 0 and Board[cd[0]][cd[1] + 1] == '-':
                # copy the path of the current cell to the neighbour, add the neighbor coordinates,
                # add "R" to the string, and enqueue the neighbor coordinates into sq
                temp_list = paths[cd[0]][cd[1]][0][:]
                temp_list.append((cd[0], cd[1] + 1))
                temp_string = paths[cd[0]][cd[1]][1] + 'R'
                paths[cd[0]][cd[1]+1] = (temp_list, temp_string)
                sq.put((cd[0], cd[1] + 1))
        # check left neighbor if exists
        if cd[1] > 0:
            # check if the neighbor cell is not visited, and has no barrier
            if len(paths[cd[0]][cd[1] - 1][0]) == 0 and Board[cd[0]][cd[1] - 1] == '-':
                # copy the path of the current cell to the neighbour, add the neighbor coordinates,
                # add "L" to the string, and enqueue the neighbor coordinates into sq
                temp_list = paths[cd[0]][cd[1]][0][:]
                temp_list.append((cd[0], cd[1] - 1))
                temp_string = paths[cd[0]][cd[1]][1] + 'L'
                paths[cd[0]][cd[1] - 1] = (temp_list, temp_string)
                sq.put((cd[0], cd[1] - 1))
    # if the function has not returned until this level, the path could not reach Destination, return None.
    return None


def main():
    Puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]
    print(solve_puzzle(Puzzle, (0, 4), (3, 4)))
    print(solve_puzzle(Puzzle, (0, 2), (2, 2)))
    print(solve_puzzle(Puzzle, (0, 0), (4, 4)))
    print(solve_puzzle(Puzzle, (0, 0), (4, 0)))

    Puzzle2 = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '#'],
        ['#', '-', '#', '#', '-'],
        ['-', '-', '-', '-', '-']
    ]
    print(solve_puzzle(Puzzle2, (0, 4), (3, 4)))


if __name__ == '__main__':
    main()
