def GUI_Menu(state, client, client_state):
    root = Tk()
    match state:
        case 0:
            state, substate = GUI_Main_Menu_Select(root, client, state, client_state)
    return state
