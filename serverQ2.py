import socket

def convertToCelcius(f):
    celc = (f - 32) * 5 / 9
    return celc

def main():
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.bind(('', 8080))
    a.listen(1)

    print("Waiting....")

    while True:
        conn, addr = a.accept()
        print(f"Connect to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f = float(data.decode())
            celc = convertToCelcius(f)
            conn.send(str(celc).encode())
        conn.close()

if __name__ == '__main__':
    main()
