<html>
<head>
<title>tcpreply</title>
<script src="/static/jquery-3.6.1.min.js"></script>
<script src="/static/index.js"></script>
<script src="/static/echarts.min.js"></script>
</head>
<body>

    上传 pcap>
    <form action="upload"method="POST" enctype="multipart/form-data">
        <input type="file"name="data" />
        <input type="submit"value="上传" />
    </form>

    删除 pcap:
    <select id="sel_del_pcap">
    % for item in file_list:
      <option value="{{item}}">{{item}}</option>
    % end
    </select>
    <button id="btn_del_pcap">删除</button>

    <br/>
    <br/>
    <br/>

    发包控制><br/>
    选择 pcap:
    <select id="pcap">
    % for item in file_list:
      <option value="{{item}}">{{item}}</option>
    % end
    </select>

    选择发包网卡：
    <select id="nic">
    % for item in nic_list:
      <option value="{{item}}">{{item}}</option>
    % end
    </select>

    <br/>
    修改源MAC: <input type="text" name="src_mac">
    修改目的MAC: <input type="text" name="dst_mac">
    (MAC格式：00:00:00:00:00:01, 为空不修改，使用包里的MAC)

    <br/>
    <button id="start_send_packet">开始发包</button>
    <button id="stop_send_packet">停止发包</button>

    <br/>
    <br/>

    状态><br/>
    运行状态：<span id="status_span">未发包</span> <br/>
    带宽 mbit/s：<span id="bps_span">0</span> <br/>

    <br/>
    <div id="div_bps_chart" style="width: 1000px;height:400px;"></div>
</body>
</html>