import os
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = os.environ.get("SQL_HOST").replace('"', "")
port = os.environ.get("SQL_PORT").replace('"', "")
result = 0
# WAIT POSTGRES TO BE ONLINE
while result == 0:
    time.sleep(1.5)
    result = sock.connect_ex((host, int(port)))
else:
    print("UP")
    # RETURN TO SHELL
    try:
        sock.close()
    except Exception as err:
        print(err)