#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
int socketClient;
struct sockaddr_in serverAddress;
int random;

// Create Socket
socketClient = socket(AF_INET, SOCK_STREAM, 0);

// Configure Address
serverAddress.sin_family = AF_INET;
serverAddress.sin_port = htons(8080);
serverAddress.sin_addr.s_addr = inet_addr("192.168.100.212");

// Connect To Server
connect(socketClient,(struct sockaddr *) &serverAddress, sizeof(serverAddress));

// Receiving Number From Server
recv(socketClient, &random, sizeof(random), 0);

// Print Out Number
printf("Random Number: %d\n", random);

// Close Client's Socket
close(socketClient);

return 0;
}
