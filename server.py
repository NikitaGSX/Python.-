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

args = parser.parse_args()

config = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024

        }

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

host        = config.get('host')
port        = config.get('port')
buffersize  = config.get('buffersize')

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server started with { host }:{ port }')

    while True:
        client, address = sock.accept()
        print(f'Client was detected { address[0] }:{ address[1] }')

        b_request = client.recv(buffersize)
        print(f'Client send message { b_request.decode() }')

        client.send(b_request)
        client.close()

except KeyboardInterrupt:
    print('\n\tServer shutdown!')

