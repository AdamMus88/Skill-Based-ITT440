import socket
def main():
    #IP and port of the server
    s_ip = "192.168.100.212"
    s_port = 8888

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    s.connect((s_ip, s_port))

    # Request a quote from server
    quote = s.recv(1024)
    print("                    QUOTES OF THE DAY!                     ")
    print("_________________________")
    print("QUOTES FOR THIS SESSION>>> %s" % quote.decode())

    # Close socket
    s.close()

main()

