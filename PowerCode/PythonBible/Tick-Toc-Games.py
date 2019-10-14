gboard = [str(' ') for i in range(9)]


def getBoard():
    print('~'*9)
    print('{} | {} | {}'.format(gboard[0], gboard[1], gboard[2]))
    print('~'*9)
    print('{} | {} | {}'.format(gboard[3], gboard[4], gboard[5]))
    print('~'*9)
    print('{} | {} | {}'.format(gboard[6], gboard[7], gboard[8]))
    print('~'*9)


def getPlayer(player):
    getBoard()
    if player == 1:
        marker = 'X'
    else:
        marker = 'O'
    print("Currently Playing : "+str(player))
    pointer = input("Select your Position: ").strip()

    if pointer.isdigit() and int(pointer) in range(1, 10):
        pointer = int(pointer)
        if gboard[pointer-1] == ' ':
            gboard[pointer-1] = marker
        else:
            print("Position already Filled. select other Position")
            print("To Exit from game Enter 'X'")
            getPlayer(player)
    elif pointer == 'X':
        exit()
    else:
        print('Invalid Position Selection. Plz Retry from (1-9)')
        print("To Exit from game Enter 'X'")
        getPlayer(player)
    winCheck(player)


def winCheck(player):
    if player == 1:
        marker = 'X'
    else:
        marker = 'O'
    if gboard[0] == gboard[1] == gboard[2] == marker or \
            gboard[3] == gboard[4] == gboard[5] == marker or \
            gboard[6] == gboard[7] == gboard[8] == marker or\
            gboard[0] == gboard[3] == gboard[6] == marker or \
            gboard[1] == gboard[4] == gboard[7] == marker or \
            gboard[2] == gboard[5] == gboard[8] == marker or \
            gboard[0] == gboard[4] == gboard[8] == marker or \
            gboard[2] == gboard[4] == gboard[6] == marker:
        print("Player {} Win!!!".format(player))
        getBoard()
        exit()
    else:
        pass


print("Lets Play Tick-Tac-Toc Game.")
for i in range(len(gboard)+1):
    if i % 2 == 0:
        player = int(i % 2)+2
        getPlayer(player)
    else:
        player = int(i % 2)
        getPlayer(player)
    