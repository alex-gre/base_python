#pip install ipaddress
#pip install psycopg2

import socket
import random
import ipaddress
from threading import Thread  # для многопоточн.
import psycopg2

def port_scan(random_ip):
    is_open = 'Port Close'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    result = sock.connect_ex((random_ip, 5432))
    if result == 0 :
        is_open = "Port Close"
    sock.close()

    return is_open

#local_test = port_scan('127.0.0.1')
#print(local_test)    
    

def get_random_ip():
    while True:
        random_ip = f'{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}'
        if not ipaddress.ip_address(random_ip).is_private:
            return random_ip
        

def start_search(thread_number):
    for count in range (1,1000):
        random_ip = get_random_ip()
        is_ip_open = port_scan(random_ip)
        print(f'[{thread_number}] {count}, - {random_ip}, - {is_ip_open}')  

#start_search() 


def run_multi_thread_search():
    for thread_number in range (1,30):
        Thread(

            target=start_search,
            args=(thread_number, )

        ).run()

#run_multi_thread_search()

open_ips = [
    '107.163.36.23',
    '164.167.23.131'
]

#def try_connect(try_ip, username, password):
def try_connect(try_ip):
    try:
        conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = 'postgres',
            host = try_ip,
            port = "5432",
            connection_timeout = 5

        )
        conn.close()
        return True

    except Exception as e:
        #print(e)    
        return  False
    
for try_ip in open_ips:
    res = try_connect(try_ip)
    print(f'{try_ip} - {res}')    
