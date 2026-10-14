
def main():
    ssh_information = GUI_ssh_information()
    client = GUI_ssh_connect(ssh_information)
    client_state = GlobalState()
    try:
        #client_state.updateDockerInformation(client)
        #print(client_state.getTeachers(client))
        state = 0
        while state is not -1:
            state = GUI_Menu(state, client, client_state)
        del client_state
    except Exception as e:
        print(f"Error: {e}")
        del client_state
    finally:
        print("Close")
        client.close()

if __name__ == "__main__":
    main()
