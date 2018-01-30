#The function counts the surrounding by how many "connections" every "cross" and "square" has.
def check_surrounding(board, size, target_count, start):
    for i in range(0, size):#row
        for j in range(0, size): #column

            count = 0
            row = start + 2*i
            col = start + 2*j
            if row < size:

                if col < size:

                    if board[row - 1][col] == 1 and row > 0:        #Under circle
                        count += 1

                    if row < size-1 and board[row + 1][col] == 1:   #Over circle
                        count += 1

                    if board[row][col - 1] == 1 and col > 0:        #Left of circle
                        count += 1

                    if col < size-1 and board[row][col + 1] == 1:   #Right of circle
                        count += 1

                    if count == target_count:
                        print(board[row][col])

                    else:
                        print("funkar ej")
                else:
                    break

            else:
                break


# -----------------------------------------------------------------------------------------------

#TODO: Test function!

#The functions controls if the given solution is one complete line (same start- and endpoint).
def check_if_complete_line(board, previous_coordinate, current_coordinate):  # In the first run previous_coordinate=None.
    start_coordinate = board.index(2)

    if row > 0: #We could do this in one expression by writing a lot of "or if's".
        if board[row - 1][col] == 1 or board[row - 1][col] == 2:
            if board[row - 1][col] != previous_coordinate:
                previous_coordinate = current_coordinate
                current_coordinate = board[row - 1][col]
                if current_coordinate == start_coordinate:
                    return True
                    print ('loop is done')
                else:
                    check_if_one_loop(previous_coordinate, current_coordinate)

    if row < size - 1 and board[row + 1][col] == 1:
        if board[row - 1][col] == 1 or board[row - 1][col] == 2:
            if board[row - 1][col] != previous_coordinate:
                previous_coordinate = current_coordinate
                current_coordinate = board[row - 1][col]
                if current_coordinate == start_coordinate:
                    return True
                    print ('loop is done')
                else:
                    check_if_one_loop(previous_coordinate, current_coordinate)

    if board[row][col - 1] == 1 and col > 0:
        if board[row - 1][col] == 1 or board[row - 1][col] == 2:
            if board[row - 1][col] != previous_coordinate:
                previous_coordinate = current_coordinate
                current_coordinate = board[row - 1][col]
                if current_coordinate == start_coordinate:
                    return True
                    print ('loop is done')
                else:
                    check_if_one_loop(previous_coordinate, current_coordinate)

    if col < size - 1 and board[row][col + 1] == 1:
        if board[row - 1][col] == 1 or board[row - 1][col] == 2:
            if board[row - 1][col] != previous_coordinate:
                previous_coordinate = current_coordinate
                current_coordinate = board[row - 1][col]
                if current_coordinate == start_coordinate:
                    return True
                    print ('loop is done')
                else:
                    check_if_one_loop(previous_coordinate, current_coordinate)