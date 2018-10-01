VALID_COMMANDS = 'C,L'

clients = 'tomas,juan,'


def create_client(client_name): #1
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in clients list')


def list_clients(): #3
    print(clients)


def _add_comma(): #2 
    global clients

    clients += ','


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name?' )
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')
