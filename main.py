import sys
import socket
# targetip = socket.gethostbyname(hostname)
port = 22

iplists = []
ipsubfix = "192.168.0"
for num in range(0,100):
    iplists.append(ipsubfix + "." + str(num))

ipcount = 0
for targetip in iplists:
    ipcount = ipcount + 1
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((targetip, port))
        if result == 0:
            print("{}:{} is open".format(targetip, port))
            sock.close()
    except KeyboardInterrupt:
        input("Press Enter to EXIT")
        sys.exit()
    # finally:
    #     print("{}:{} is closed".format(targetip, port))
input("Press Enter to EXIT")


# ========Todo========
# 1. ping 구현        done
# 2. tcp ping 구현    done
# 3. 나라별 ip range