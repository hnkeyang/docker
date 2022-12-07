$(document).ready(function(){
    $("#start_send_packet").click(function(){
        let pcap_name = $("#pcap").val();
        let nic_name = $("#nic").val();

        var regex_mac = new RegExp('([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}');

        let src_mac = $("input[name='src_mac']").val();
        if (!src_mac)
        {
          src_mac="00:00:00:00:00:00";
        }

        let dst_mac = $("input[name='dst_mac']").val();
        if (!dst_mac)
        {
          dst_mac="00:00:00:00:00:00";
        }

        if (!regex_mac.test(src_mac))
        {
          alert("源MAC格式不对: " + src_mac);
          return;
        }

        if (!regex_mac.test(dst_mac))
        {
          alert("目的MAC格式不对: " + dst_mac);
          return;
        }

        let url = "/ctrl/start/";
        url += pcap_name;
        url += "/";
        url += nic_name;
        url += "/";
        url += src_mac;
        url += "/";
        url += dst_mac;
        
        $.get(url,function(data, status){
          //alert("状态: " + data);
          alert("开始发包");
        });

        
        $("#status_span").html("发包中");
    });
});

$(document).ready(function(){
    $("#stop_send_packet").click(function(){
        let url = "/ctrl/stop";
        
        $.get(url,function(data, status){
          //alert("状态: " + data);
          alert("停止发包");
        });
    });
});

$(document).ready(function(){
  $("#btn_del_pcap").click(function(){
      let pcap_file = $("#sel_del_pcap").val();

      let url = "/del_pcap/";
      url += pcap_file;
      
      $.get(url,function(data, status){
        if (status == "success")
        {
          let pos = "#sel_del_pcap option[value=\'" + pcap_file + "\']";
          $(pos).remove();
          alert(pcap_file + " 删除成功");
        }
      });
  });
});


// 状态
$(document).ready(function(){
  let last_tx_total_byte = 0;
  let bps = 0;
  let status = "未发包"

  var bpsChart = echarts.init(document.getElementById('div_bps_chart'));
  var option = {
    xAxis: {
      data: [] // label
    },
    yAxis: {},
    series: [
      {
        data: [], // data
        type: 'line',
        smooth: true
      }
    ]
  };

  let n = 1;
  let base = 0;
  let count = 5;

  setInterval(function(){
      let url = "/status";
      $.getJSON(url,function(data){
          if (data.status == "running"){
            status = "发包中"
          }
          else {
            status = "未发包"
          }
          $("#status_span").html(status);
          if (last_tx_total_byte != 0) {
            bps = (data.tx_total_byte - last_tx_total_byte) * 8 / 3/1024/1024;
            $("#bps_span").html(bps.toFixed(2));

            
            option["xAxis"]["data"].push(n);
            option["series"][0]["data"].push(bps);
            console.log(n, base, count);
            if (n - base > count)
            {
              base += 1;
              option["xAxis"]["data"].shift();
              option["series"][0]["data"].shift();
            }

            bpsChart.setOption(option);

            n++;
          }
          last_tx_total_byte = data.tx_total_byte
      });
      
  },3000);
});
