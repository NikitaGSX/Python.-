#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import json
import socket
import argparse
from datetime import datetime

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

    action = input('Enter actoin:\n\t')
    data = input('Enter data:\n\t')

    request = {
            'action': action,
            'time': datetime.now().timestamp(),
            'data': data
            }

    str_request = json.dumps(request)
    sock.send(str_request.encode())

    b_response = sock.recv(buffersize)
    print(f'Server send data: \n\t { b_response.decode() }')

except KeyboardInterrupt:
    print('\n\tClient shutdown!')



