#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import socket
import argparse

parser = argparse.ArgumentParser(description='Process some integers.') # Изменил строчку кода следуя примерам из документации
parser.add_argument(
        '-c', '--config', type=str, required=False,
        help='Sets config file path'
        )

args    = parser.parse_args()
config  = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024
        }


host        = config.get('host')
port        = config.get('port')
buffersize  = config.get('buffersize')

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

try:
    sock = socket.socket()
    sock.connect((host, port))
    print(f'Client started with { host }:{ port }')

    data = input('Enter data: ')
    sock.send(data.encode())

    b_response = sock.recv(buffersize)
    print(f'Server send data: \n\t { b_response.decode() }')

except KeyboardInterrupt:
    print('\n\tClient shutdown!')



