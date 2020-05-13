

def getBroadcasters(currQueue, i):
    for j in range(len(currQueue)):
        if (i % len(currQueue)) != j:
            print(currQueue[j])

def main():
    queue = ["Bar", "Amitai", "Ronen", "Saar"]
    while(1):
        print("type 'get' to get curr broadcasters, 'exit' to exit\n")
        string = input()
        if string == 'get':
            gamenum = int(input("Which game is it (number in series): " )) - 1
            getBroadcasters(queue, gamenum)
        if string == 'exit':
            break;


main()
