import socket

def main():
    b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b.connect(('192.168.100.212', 8080))

    f = float(input("Please enter current temperature in Fahrenheit: "))
    b.send(str(f).encode())

    celc = b.recv(1024).decode()
    print(f"Current temperature in Celcius: {celc}")

    b.close()

if __name__ == '__main__':
    main()

