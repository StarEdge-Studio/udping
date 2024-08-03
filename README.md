# UDPing

UDPing is a simple command-line tool for testing network latency and connectivity using UDP packets. It supports both IP addresses and domain names.

## Features

- Send UDP packets to test network latency
- Compatible with both IP addresses and domain names
- Provides detailed ping statistics similar to the traditional `ping` tool

## Getting Started

### For End Users

Pre-compiled executables for various platforms are available on the [releases](https://github.com/shing-yu/udping/releases) page. 
Download the appropriate version for your system and extract the archive. Follow the instructions below to run the server and client.

You can add the executable to your system's PATH to run it from any directory.

#### Running the Server (Optional)

To run the UDPing server, use the following command in your terminal or command prompt:

```shell
./udping_server 0.0.0.0 12345
```

This will start the server listening on all network interfaces on port `12345`.

#### Running the Client

To run the UDPing client, use the following command in your terminal or command prompt:

```shell
./udping <host> <port> [options]
```

Replace `<host>` with the server's IP address or domain name, `<port>` with the server's port.

Use "-h" or "--help" to see the full list of options.

Example:

```shell
./udping example.com 12345 -c 5 -i 1
```

This will send 5 ping requests to `example.com` on port `12345`, with an interval of 1 second between each request.

### Output

The client will output results similar to the traditional `ping` tool, sequence number and round-trip time (RTT). It will also provide summary statistics at the end.

Example output:

```
Ping udp://127.0.0.1:12345 [127.0.0.1] with 5 packets:

Reply from 127.0.0.1:12345 : seq=0 time=25.45 ms
Reply from 127.0.0.1:12345 : seq=1 time=25.52 ms
Reply from 127.0.0.1:12345 : seq=2 time=25.64 ms
Reply from 127.0.0.1:12345 : seq=3 time=25.97 ms
Reply from 127.0.0.1:12345 : seq=4 time=25.71 ms

--- udp://127.0.0.1:12345 ping statistics ---

5 packets transmitted, 5 received, 0 lost.
(0.0% loss)

rtt min=25.45 ms, avg=25.66 ms, max=25.97 ms
```

## Development

### Prerequisites

- Python 3.x

### Installation

Clone the repository:
```shell
git clone https://github.com/shing-yu/udping.git
cd udping
```

### Running the Server

To run the UDPing server, use the following command:

```shell
python src/udping_server.py <host> <port>
```

### Running the Client

To run the UDPing client, use the following command:

```shell
python src/udping.py <host> <port> [options]
```

Replace `<host>` with the server's IP address or domain name, `<port>` with the server's port.

Use "-h" or "--help" to see the full list of options.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
