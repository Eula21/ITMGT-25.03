'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_followed = list(social_graph[from_member]["following"])
    to_followed = list(social_graph[to_member]["following"])

    i = 0
    from_bool = 0
    
    for i in range(0, len(from_followed)):
        if to_member == from_followed[i]:
            from_bool += 1
            break

    i = 0
    to_bool = 0

    for i in range(0, len(to_followed)):
        if from_member == to_followed[i]:
            to_bool += 1
            break

    if (from_bool == 1) and (to_bool == 1):
        status = "friends"
    elif from_bool == 1:
        status = "follower"
    elif to_bool == 1:
        status = "followed by"
    else:
        status = "no relationship"

    return status


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    lines = []

    for x in range(0, len(board)):
        h_lines = board[x]
        lines.append(h_lines)

    for x in range(0, len(board)):
        v_lines = []
        for y in range(0, len(board)):
            v_element = board[y][x]
            v_lines.append(v_element)
        lines.append(v_lines)

    x = 0
    dup_lines = []
    
    for x in range(0, len(board)):
        dup_element = board[x][x]
        dup_lines.append(dup_element)
    lines.append(dup_lines)

    x = 0
    ddown_lines = []
    
    for x in range(0, len(board)):
        ddown_element = board[x][len(board) - 1 - x]
        ddown_lines.append(ddown_element)
    lines.append(ddown_lines)

    X_correct_pat = []

    for i in range(0, len(board)):
        X_correct_pat.append("X")

    O_correct_pat = []

    for i in range(0, len(board)):
        O_correct_pat.append("O")

    status = "NO WINNER"

    for l in lines:
        if l == X_correct_pat:
            status = "X"
            break
        elif l == O_correct_pat:
            status = "O"
            break
    
    return status


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0

    for l in route_map.keys():
        if l == (first_stop, second_stop):
            travel_time = route_map[first_stop, second_stop]["travel_time_mins"]
            break
    
    keys = list(route_map.keys())

    if travel_time == 0:
        for i in range(0, len(route_map)):
            if keys[i][0] == first_stop:
                travel_time += route_map[keys[i]]["travel_time_mins"]
                if keys[i] == (first_stop, second_stop):
                    break
                else:
                    first_stop = keys[i][1]
                    if (i == (len(route_map) - 1)) and (keys[len(route_map) - 1] != (first_stop, second_stop)):
                        i = 0
                        for i in range(0, len(route_map)):
                            if keys[i][0] == first_stop:
                                travel_time += route_map[keys[i]]["travel_time_mins"]
                                if keys[i] == (first_stop, second_stop):
                                    break
                                else:
                                    first_stop = keys[i][1]
    
    return travel_time