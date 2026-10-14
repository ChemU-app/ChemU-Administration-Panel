def GUI_ssh_information():
    
    ssh_address = ""
    ssh_username = ""
    ssh_key_file = ""

    root = Tk()
    root.title('Submit SSH Information')
    root.resizable(True, True)
    root.geometry('800x600')

    def select_SSH_Key():
        nonlocal ssh_key_file
        file_types = [
            ("PEM files", "*.pem")
        ]
        ssh_key_file = fd.askopenfilename(
            title='Open a ssh key',
            initialdir='.',
            filetypes=file_types
        )

    def getInputValues():
        nonlocal ssh_address
        nonlocal ssh_username
        ssh_address = server_address_box.get("1.0", "end-1c")
        ssh_username = server_username_box.get("1.0", "end-1c")
        root.quit()

    address_label = Label(
        root,
        text="Server Address:"
    )
    address_label.pack(expand=True)
    server_address_box = Text(
        root,
        height=1,
        width=50
    )
    server_address_box.pack()
    username_label = Label(
        root,
        text="Username:"
    )
    username_label.pack()
    server_username_box = Text(
        root,
        height=1,
        width=50
    )
    server_username_box.pack()

    button = ttk.Button(
        root,
        text='Select a ssh key',
        command=select_SSH_Key
    )
    button.pack()
    connect_button = ttk.Button(
        root,
        text='Connect',
        command=getInputValues
    )
    connect_button.pack()
    

    root.mainloop()
    root.destroy()
    return [
        ssh_address,
        ssh_username,
        ssh_key_file
    ]
