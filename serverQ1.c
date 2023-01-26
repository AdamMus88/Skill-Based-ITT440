#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
int socketServer, socketClient, random;
struct sockaddr_in serverAddress, addressClient;
int clientAddressLength = sizeof(addressClient);

// Create Socket
socketServer = socket(AF_INET, SOCK_STREAM, 0);
if (socketServer == -1){
        printf("Failed!...\n");
        exit(0);
}
else
        printf("Completed!...\n");
        bzero(&serverAddress, sizeof(serverAddress));

// Configure Address
serverAddress.sin_family = AF_INET;
serverAddress.sin_port = htons(8080);
serverAddress.sin_addr.s_addr = INADDR_ANY;

// Bind Socket To Address
if((bind(socketServer, (struct sockaddr *) &serverAddress, sizeof(serverAddress))) != 0){
        printf("Failed To Bind!...\n");

}
else
        printf("Completed Bind!...\n");

// Listen Incoming Connections
if((listen(socketServer, 5)) != 0) {
        printf("Failed...\n");

}
else
        printf("Listening...\n");

while (1) {
// Accept Incoming Connection
socketClient = accept(socketServer, (struct sockaddr *) &addressClient,
&clientAddressLength);
if(socketClient < 0){
        printf("Connection Failed!...\n");

}
else
        printf("Connected!...\n");

// Random Number Will Generate
srand(time(0));
random = rand() % 900 + 100;

//Random Number Will Be Send To Client
send(socketClient, &random, sizeof(random), 0);
// Closing Socket's Client
close(socketClient);
}

// Closing Socket's Server
close(socketServer);

return 0;
}
