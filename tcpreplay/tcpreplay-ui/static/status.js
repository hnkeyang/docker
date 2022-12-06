$(document).ready(function(){
    
    let last_tx_total_byte = 0;
    let bps = 0;
    setInterval(function(){
        let url = "/get_nic_tx_total_byte";
        $.get(url,function(data, status){
            //alert("rx: " + data);
            
            bps = parseInt(data) * 8 - last_tx_total_byte;
            $("#bps_span").html(bps);
            last_tx_total_byte = parseInt(data) * 8
        });
        
    },3000);
});

