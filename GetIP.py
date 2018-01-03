import requests
import re
from bs4 import BeautifulSoup
from ipaddress import IPv4Network

def Range(ASN = "AS4766"): # Autonomous System Number, ASN (LG AS4766) (KT AS4766)
    '''
    This function is getting list of ip range through ASN
    '''
    url = "http://www.cidr-report.org/cgi-bin/as-report?as={}&view=2.0".format(ASN)
    rawHtml = re.findall(r'AS\.<p>\n<pre>(.*?)</a>\n</pre>\n<p>', requests.get(url).text.replace('  ',''), re.S)
        # Get an A Tag from raw html
    IPs = set()
    for ip in BeautifulSoup(rawHtml[0], "html.parser").find_all("a", class_="green"):
        IPs.add(ip.get_text())  # IP range text parse from raw html
    return sorted(IPs)  # Return sorted IP set

def List(ipRange):
    '''
    This function is 
    '''
    iplist = []
    for addr in IPv4Network(ipRange):
        iplist.append(str(addr))
    return iplist

if __name__ == "__main__":
    pass