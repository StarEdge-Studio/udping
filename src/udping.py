import socket
import time
import argparse


red = "\033[1;31m"
yellow = "\033[1;33m"
green = "\033[1;32m"
reset = "\033[0m"
__version__ = "v0.2.0-dev.1"


def resolve_host(host):
    """Resolve the host to an IP address."""
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror as e:
        print(f"Error resolving host {host}: {e}")
        return None


def udping_client(host, port, count, interval, timeout=1):
    ip = resolve_host(host)
    if ip is None:
        print("Failed to resolve host. Exiting.")
        return

    server_address = (ip, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    # TODO: Add proxy support

    seq = 0
    rtts = []

    print(f"\nPing udp://{host}:{port} [{ip}] with {count} packets:\n")

    try:
        while seq < count:
            message = f"PING {seq} {time.time()}"
            # noinspection PyBroadException
            try:
                start_time = time.time()
                sock.sendto(message.encode(), server_address)
                data, _ = sock.recvfrom(1024)
                end_time = time.time()
                rtt = (end_time - start_time) * 1000  # convert to milliseconds
                rtts.append(rtt)
                print(f"Reply from {ip}:{port} : seq={seq} time={rtt:.2f} ms")
            except socket.timeout:
                print(yellow + f"Request timed out, seq={seq}" + reset)
            except Exception:
                print(yellow + f"Request failed, seq={seq}" + reset)

            seq += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        # print("\nPing terminated by user.")
        print(red + "\nPing interrupted by user." + reset)
        print(f"\n--- udp://{host}:{port} ping statistics (interrupt) ---\n")
    else:
        print(f"\n--- udp://{host}:{port} ping statistics ---\n")

    # print("\n--- {} ping statistics ---".format(host))
    packets_transmitted = seq
    packets_received = len(rtts)
    packet_lost_count = packets_transmitted - packets_received
    packet_loss = ((packets_transmitted - packets_received) / packets_transmitted) * 100
    # print(f"{packets_transmitted} packets transmitted, "
    #       f"{packets_received} received, "
    #       f"{packet_loss:.1f}% packet loss\n")
    print(f"{packets_transmitted} packets transmitted, "
          f"{packets_received} received, "
          f"{packet_lost_count} lost.")
    if packet_loss == 0:
        print(green + f"({packet_loss:.1f}% loss)\n" + reset)
    elif packet_loss < 80:
        print(yellow + f"({packet_loss:.1f}% loss)\n" + reset)
    else:
        print(red + f"({packet_loss:.1f}% loss)\n" + reset)

    if rtts:
        min_rtt = min(rtts)
        max_rtt = max(rtts)
        avg_rtt = sum(rtts) / len(rtts)
        # print(f"rtt min/avg/max = {min_rtt:.2f}/{avg_rtt:.2f}/{max_rtt:.2f} ms")
        print(f"rtt min={min_rtt:.2f} ms, avg={avg_rtt:.2f} ms, max={max_rtt:.2f} ms\n")
    else:
        print("No RTT data available.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDPing Client")
    parser.add_argument("host", type=str, help="Server host to ping (IP or domain name)")
    parser.add_argument("port", type=int, help="Server port to ping")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-c", "--count", type=int, default=5, help="Number of pings to send")
    parser.add_argument("-f", "--forever", action="store_true",
                        help="Ping the server forever (will cover the count option)")
    parser.add_argument("-i", "--interval", type=float, default=1, help="Interval between pings in seconds")
    parser.add_argument("-t", "--timeout", type=float, default=1, help="Timeout for waiting for a response in seconds")
    parser.add_argument("-w", "--wait", type=float, default=1, help="Timeout for waiting for a response in seconds")
    parser.add_argument("-p", "--proxy", type=str, help="Use a proxy server to ping the target (protocol://host:port)")
    parser.add_argument("-dc", "--disable-color", action="store_true", help="Disable colored output")

    args = parser.parse_args()

    if args.disable_color:
        red = yellow = green = reset = ""
    times = args.count if not args.forever else float("inf")

    udping_client(args.host, args.port, times, args.interval, args.timeout)
