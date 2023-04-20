<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Send packet with Scapy</title>
</head>
<body>
    <h1>Send packet with Scapy</h1>
    <form action="/sendpacket" method="post">
        <p>
            <label>选择发包网卡: </label>
            <select name="iface">
            % for item in nic_list:
              <option value="{{item}}">{{item}}</option>
            % end
            </select>
        </p>
        <p>
            <label>Source MAC address: </label>
            <input type="text" name="src_mac" value="0:0c:29:86:bd:ac">
        </p>
        <p>
            <label>Destination MAC address: </label>
            <input type="text" name="dst_mac" value="0:0c:29:86:bc:ac">
        </p>
        <p>
            <label>Source IP address: </label>
            <input type="text" name="src_ip" value="192.168.1.1">
        </p>
        <p>
            <label>Destination IP address: </label>
            <input type="text" name="dst_ip" value="114.114.115.115">
        </p>
        <p>
            <label>Protocol: </label>
            <select name="protocol">
                <option value="ICMP">ICMP</option>
                <option value="TCP">TCP</option>
                <option value="UDP">UDP</option>
            </select>
        </p>
        <p>
            <label>Packet length: </label>
            <input type="text" name="length" value="50">
        </p>
        <p>
            <label>TCP flags (only for TCP protocol): </label>
            <select name="flags">
                <option value="syn">SYN</option>
                <option value="ack">ACK</option>
                <option value="push">PUSH</option>
            </select>
        </p>
        <p>
            <input type="submit" value="Send packet">
        </p>
    </form>
</body>
</html>

