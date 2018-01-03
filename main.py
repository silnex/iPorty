import sys
import socket
import GetIP

def iPortyScan(ASNumber = "AS4766", port = "22"):
    '''
    ASNumber is Autonomous System Number,
    port value is 
    'AS4766' is LG AS Number
    '''
    iplists = GetIP.List(GetIP.Range(ASNumber))
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
    iPortyScan()
'''
South Korea ISP ASN list
http://www.cidr-report.org/cgi-bin/as-report?as=AS4766&view=2.0
http://www.cidr-report.org/cgi-bin/as-report?as=AS9318&view=2.0
http://www.cidr-report.org/cgi-bin/as-report?as=AS38091&view=2.0
http://www.cidr-report.org/cgi-bin/as-report?as=AS17858&view=2.0
'''