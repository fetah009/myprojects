import socket


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False

    return True


def is_valid_port(begin_port, end_port):
    if (begin_port < 1 and end_port > 65353):
        return False
    return True


def scan(ip, begin_port, end_port):
    open_ports = []
    for port in range(begin_port, end_port+1):
        s = socket.socket()
        try:

            s.connect((ip, port))
            print("[!] port "+str(port), " is open | service :" +
                  socket.getservbyport(port))
            open_ports.append(str(port))
        except:
            print("[X] port " + str(port) + " closed")
        finally:
            s.close()

    print("****************************")
    print("the open ports are : ")
    for i in open_ports:
        print("port "+i+" | " + "service : "+socket.getservbyport(int(i)))

    print("****************************")
