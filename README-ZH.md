# UDPing

UDPing 是一个简单的命令行工具，用于通过 UDP 包测试网络延迟和连接性。它支持 IP 地址和域名。

## 特性

- 发送 UDP 包测试网络延迟
- 兼容 IP 地址和域名
- 提供类似于传统 `ping` 工具的详细 ping 统计信息

## 入门指南

### 针对终端用户

各种平台的预编译可执行文件可在 [releases](https://github.com/shing-yu/udping/releases) 页面下载。
下载适合您系统的版本并解压，然后在终端或命令提示符中运行可执行文件。

您可以将可执行文件添加到系统的 PATH 以便从任何目录运行它。

#### 运行服务器（可选）

要运行 UDPing 服务器，请在终端或命令提示符中使用以下命令：

```shell
./udping_server 0.0.0.0 12345
```

这将启动服务器并监听所有网络接口上的 `12345` 端口。

#### 运行客户端

要运行 UDPing 客户端，请在终端或命令提示符中使用以下命令：

```shell
./udping <host> <port> [options]
```

将 `<host>` 替换为服务器的 IP 地址或域名，将 `<port>` 替换为服务器的端口。

使用 "-h" 或 "--help" 查看完整的选项列表。

示例：

```shell
./udping example.com 12345 -c 5 -i 1
```

这将向 `example.com` 上的 `12345` 端口发送 5 次 ping 请求，每次请求之间间隔 1 秒。

### 输出

客户端将输出类似于传统 `ping` 工具的结果，包含序列号和往返时间（RTT）。它还将在最后提供总结统计信息。

示例输出：

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

## 开发

### 先决条件

- Python 3.x

### 安装

克隆仓库：
```shell
git clone https://github.com/shing-yu/udping.git
cd udping
```

### 运行服务器

要运行 UDPing 服务器，请使用以下命令：

```shell
python src/udping_server.py <host> <port>
```

### 运行客户端

要运行 UDPing 客户端，请使用以下命令：

```shell
python src/udping.py <host> <port> [options]
```

将 `<host>` 替换为服务器的 IP 地址或域名，将 `<port>` 替换为服务器的端口。

使用 "-h" 或 "--help" 查看完整的选项列表。

## 贡献

欢迎贡献！请打开一个 issue 或提交一个 pull request 进行您的更改。

## 许可证

本项目根据 MIT 许可证授权。详情请参见 [LICENSE](LICENSE) 文件。