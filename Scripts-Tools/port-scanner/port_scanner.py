#!/usr/bin/env python3 

import socket
import sys 
from datetime import datetime

target = input("Masukkan IP Target: ")
port_range = range(1, 1025)
timeout = 1

print("-" * 50)
print(f"Port Scanner dimulai pada: {datetime.now()}")
print(f"Target: {target}")
print("-" * 50)

try:
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"port {port}: Terbuka")
        sock.close()
        
except KeyboardInterrupt:
    print("\nScan dihentikan oleh pengguna.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname tidak dapat di-resolve")
    sys.exit()
    
except socket.error:
    print("Tidak dapat terhubung ke server.")
    sys.exit()
    
print("-" * 50)
print("Scan selesai.")