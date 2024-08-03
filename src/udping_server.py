import socket
import argparse


__version__ = "v0.2.0-dev.1"


def udping_server(host, port):
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    print(f"Listening on {host}:{port}")

    while True:
        data, address = sock.recvfrom(1024)
        print(f"Received {data.decode()} from {address}")
        sock.sendto(data, address)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDPing Server")
    parser.add_argument("host", type=str, help="Host to bind the server")
    parser.add_argument("port", type=int, help="Port to bind the server")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    udping_server(args.host, args.port)
