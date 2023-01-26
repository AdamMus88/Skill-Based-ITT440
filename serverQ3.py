import random
import threading
import socket

#array of quotes
quotes = ["Today's pain is powerful's tomorrow."
,
"Be patient with yourself. Self-growth is tender;it's holy ground. There's no greater investment.",
"Without hustle, talent will only carry you so far."]

#random quotes from array and send to client
def handle_client(sockfd):
    quote = random.choice(quotes)
    sockfd.sendall(quote.encode())
    sockfd.close()

def main():
    #server ip and port
    bindIp = "192.168.100.212"
    bindPort = 8888

    #create and bind socket
    y = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    y.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    y.bind((bindIp, bindPort))

    #listen for client
    y.listen(6)
    print("Quotes has been send to >>>>>  %s:%d" % (bindIp, bindPort))
    #start connections and execute handle_client function
    while True:
        client, addr = y.accept()
        print("Successful to connect %s" % str(addr))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


main()
