def GUI_ssh_connect(ssh_information):
    
    root = Tk()
    root.title('Connecting to:' + ssh_information[0])
    root.resizable(True, True)
    root.geometry('800x600')

    connecting = Label(
        root,
        text="CONNECTING"
    )

    connecting.pack(expand=True)

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    print(ssh_information[0])
    print(ssh_information[1])
    print(ssh_information[2])
    client.connect(
        hostname=ssh_information[0],
        username=ssh_information[1],
        key_filename=ssh_information[2]
    )

    
    root.destroy()
    return client
