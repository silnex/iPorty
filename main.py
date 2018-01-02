import sys
import socket
# targetip = socket.gethostbyname(hostname)

def GetIPlists(iprefix = "192.168.0"):
    ''' GetIPlists is return IP list all of last 8bit (except 0 and 255)
    GetIPlists will change return list that IPs from ASN     '''
    iplists = []
    for num in range(0,255):
        iplists.append(iprefix + "." + str(num))
    return iplists

def main():
    # iprefix = sys.argv[1]
    # port = sys.argv[2]
    iprefix = "192.168.0"
    port = sys
    iplists = GetIPlists(iprefix)
    for targetip in iplists:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)    # set time out 0.5sec
            result = sock.connect_ex((targetip, port))
            if result == 0:
                print("{}:{} is open".format(targetip, port))
                sock.close()
        except KeyboardInterrupt:
            input("Press Enter to EXIT")
            sys.exit()
    input("Press Enter to EXIT")

if __name__ == "__main__":
    main()