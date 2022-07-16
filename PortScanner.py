#!/usr/bin/python3
import socket
import argparse
import subprocess as ss
import requests
import sys
parser=argparse.ArgumentParser(description="THIS IS A PORT SCANNER ")
parser.add_argument("-host",type=str,help="provide domain or IP", required=True)
parser.add_argument("-port",type=str,help="provide ports you want to scan", required=True)
results = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

t_host = results.host
t_port = results.port

def connect(port):
    
        if scan(port):
            print("--------------------------------")
            print("port {} is open".format(port))
            print("output", e)
            print("--------------------------------")
        else:
            print("port {} is close".format(port))
            print("--------------------------------")
    
def scan(port):
            try:
                global e
                s.connect((t_host, int(port)))
                e = s.recv(1024)
                return True
            except:
                return False
            finally:
                s.close
        
###for single and mutiple ports 
if "," in t_port:
    for port in t_port.split(","): 
        connect(port)

###for range of ports
elif "-" in t_port:
    port_r1 = int(t_port.split("-")[0])
    port_r2 = int(t_port.split("-")[1])
    for port in range(port_r1, port_r2+1):
        connect(port)
        
#for one single port        
else:
    connect(t_port)
        
