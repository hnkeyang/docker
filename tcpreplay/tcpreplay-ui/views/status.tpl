<html>
<head>
<title>tcpreply</title>
<script src="/static/jquery-3.6.1.min.js"></script>
<script src="/static/status.js"></script>

</head>
<body>
    当前状态：
    % if status["status"] == "running":
    发包中 <br/>
    % else:
    未发包 <br/>
    % end
    带宽监控><br/>

    bps: <span id="bps_span"></span>
</body>
</html>