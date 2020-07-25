from portscanlib import *

ip = str(input("enter your ip address to scan\n"))
if(is_valid_ipv4_address(ip)):

    begin_port = int(
        input("enter your range of port to scan (start_port , end_port)\n"))
    end_port = int(input(""))
    if (is_valid_port(begin_port, end_port)):

        scan(ip, begin_port, end_port)
    else:
        print("invalid port number")
        exit()
else:
    print("invalid ip address")
