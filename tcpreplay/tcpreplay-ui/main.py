from bottle import route, run
from bottle import template, request, static_file
import threading
import os
import json

upload_path='./pcap'
static_root='static'

run_status = {
    "nic": "null",
    "status": "stoped"
}

def run_tcpreplay(pcap_file, nic, src_mac, dst_mac):
    cmd_nic_up = 'ip link set %s up' % nic
    os.system(cmd_nic_up)

    #cmd = "nohup tcpreplay -K -i %s pcap/%s > /dev/null &" % (nic, pcap_file)
    #cmd = "tcpreplay -K -i %s pcap/%s" % (nic, pcap_file)
    options=""
    if src_mac != "00:00:00:00:00:00":
        options += "--enet-smac=%s" % src_mac
    if dst_mac != "00:00:00:00:00:00":
        options += " --enet-dmac=%s" % dst_mac

    cmd = "tcpreplay-edit -K %s -i %s pcap/%s" % (options, nic, pcap_file)
    print("cmd: ", cmd)
    os.system(cmd)
    run_status["status"] = "stoped"

def stop_tcpreplay():
    #os.system('killall tcpreplay')
    os.system('killall tcpreplay-edit')

def get_dir_file_list(path):
    file_list = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if not os.path.isfile(f):
            continue

        file = f.split('/')[-1]
        if file.endswith("cap") or file.endswith("capng"):
            file_list.append(file)

    return file_list

def get_nic_list():
    nic_list = []
    with open('/proc/net/dev') as f:
        line = f.readline()
        while line is not None and line != '':
            if ':' not in line:
                line = f.readline()
                continue

            nic = line.split(':')[0].strip()

            if nic != 'lo':
                nic_list.append(nic)

            line = f.readline()

    nic_list.sort()
    return nic_list

def get_nic_tx_total_byte(nic_name):
    tx_total_byte = 0
    with open('/proc/net/dev') as f:
        line = f.readline()
        while line is not None and line != '':
            if ':' not in line:
                line = f.readline()
                continue

            nic = line.split(':')[0].strip()

            if nic_name == nic:
                tx_total_byte = line.split()[9]
                break

            line = f.readline()

    return tx_total_byte

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=static_root)

@route('/index_frame')
def index():
    return template('index_frame')

@route('/')
def index():
    return template('index',
        file_list=get_dir_file_list(upload_path),
        nic_list=get_nic_list(),
        status=run_status)

@route('/status_page')
def status():
    return template('status', status=run_status)

@route('/upload',method='POST')
def do_upload():
    uploadfile = request.files.get('data')
    uploadfile.save(upload_path,overwrite=True)
    return template('upload_success.tpl', filename = uploadfile.filename)

@route('/ctrl')
def ctrl():
    pass

@route('/ctrl/start/<pcap_name>/<nic_name>/<src_mac>/<dst_mac>')
def ctrl_start(pcap_name, nic_name, src_mac, dst_mac):
    run_status["nic"] = nic_name
    run_status["status"] = "running"
    print("start")
    print('src_mac: ', src_mac)
    print('dst_mac: ', dst_mac)
    #run_tcpreplay(pcap_name, nic_name)
    t = threading.Thread(target=run_tcpreplay, args=(pcap_name, nic_name, src_mac, dst_mac), name='RunThread')
    t.start()
    return "start"

@route('/ctrl/stop')
def ctrl_stop():
    run_status["status"] = "stoped"
    print("stop")
    stop_tcpreplay()
    return "stop"

@route('/status')
def status():
    if run_status["nic"] != "null":
        run_status['tx_total_byte'] = get_nic_tx_total_byte(run_status["nic"])
    else:
        run_status['tx_total_byte'] = 0

    return json.dumps(run_status)

@route('/get_nic_tx_total_byte')
def status():
    if run_status["nic"] != "null":
        return get_nic_tx_total_byte(run_status["nic"])
    else:
        return "0"

@route('/del_pcap/<pcap_name>')
def status(pcap_name):
    pcap_file_path = "pcap/%s" % pcap_name

    print(pcap_file_path)
    os.remove(pcap_file_path)

    return "ok"

@route('/t')
def status():
    return get_nic_tx_total_byte("veth0")

if __name__ == '__main__':
    stop_tcpreplay()
    run(host='0.0.0.0', port=80, debug=True, reloader=True)
