def GUI_Teacher_Menu(root, client, state, client_state):
    root.title('Teacher Menu')
    root.resizable(True, True)
    root.geometry('800x600')

    state=0
    sub_state=0

    label = Label(
        root,
        text="SELECT AN OPTION ON A TEACHER"
    )
    label.pack()



    def setState(newState):
        nonlocal state
        state = newState
        root.quit()

    teacherButton = ttk.Button(
        root,
        text='Teachers',
        command= lambda: setState(1)
    )
    teacherButton.grid(
        row=1,
        column=0
    )

    def exit():
        nonlocal state
        state=-1
        root.quit()

    exitButton = ttk.Button(
        root,
        text='Disconnect',
        command=exit
    )

    exitButton.grid(row=2)

    root.mainloop()
    root.destroy()
    return state, sub_state

