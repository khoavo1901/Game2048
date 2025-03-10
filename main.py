import reference

if __name__ == "__main__":
    mat = reference.start_game()
    while(True):

        # taking the user input
        # for next step
        x = input("Press the command : ")

        # we have to move up
        if(x == 'W' or x == 'w'):

            # call the move_up function
            mat, flag = reference.move_up(mat)

            # get the current state and print it
            status = reference.get_current_state(mat)
            print(status)

            # if game not over then continue
            # and add a new two
            if(status == 'GAME NOT OVER'):
                reference.add_new_2(mat)

            # else break the loop 
            else:
                break

        # the above process will be followed
        # in case of each type of move
        # below

        # to move down
        elif(x == 'S' or x == 's'):
            mat, flag = reference.move_down(mat)
            status = reference.get_current_state(mat)
            print(status)
            if(status == 'GAME NOT OVER'):
                reference.add_new_2(mat)
            else:
                break

        # to move left
        elif(x == 'A' or x == 'a'):
            mat, flag = reference.move_left(mat)
            status = reference.get_current_state(mat)
            print(status)
            if(status == 'GAME NOT OVER'):
                reference.add_new_2(mat)
            else:
                break

        # to move right
        elif(x == 'D' or x == 'd'):
            mat, flag = reference.move_right(mat)
            status = reference.get_current_state(mat)
            print(status)
            if(status == 'GAME NOT OVER'):
                reference.add_new_2(mat)
            else:
                break
        else:
            print("Invalid Key Pressed")

        # print the matrix after each
        # move.
        for row in mat:
            print(row)
