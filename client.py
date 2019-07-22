#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import socket
from argparse import ArgumentParser

parser = ArgumentParser()
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
parser      = ArgumentParser()

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

try:
    sock = socket.socket()
    sock.connect((host, port))
#    print('Client was started')

    data = input('Enter data: ')
    sock.send(data.encode())
#   print(f'Client send { data }')
    b_response = sock.recv(buffersize)
    print(f'Server send data: \n\t { b_response.decode() }')

except KeyboardInterrupt:
    print('\n\tClient shutdown!')



