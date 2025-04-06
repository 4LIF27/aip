import subprocess
import time
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection

def main(ip_address='192.168.8.1', username='admin', password='admin'):
    def get_wan_info(client):
        wan_info = client.device.information()
        return wan_info.get('WanIPAddress'), wan_info.get('DeviceName')

    with Connection(f'http://{username}:{password}@{ip_address}/') as connection:
        client = Client(connection)
        wan_ip, device_name = get_wan_info(client)
        print("Modem Name:", device_name)
        print("Modem IP:", wan_ip)
        print(client.device.reboot())
     
    time.sleep(10)
    cek(ip_address)

    with Connection(f'http://{username}:{password}@{ip_address}/') as connection:
        client = Client(connection)
        wan_ip, device_name = get_wan_info(client)
        print("Modem Name:", device_name)
        print("Modem IP:", wan_ip)

def cek(ip_address='192.168.8.1'):
    while True:
        try:
            output = subprocess.check_output(['ping', '-c', '1', ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
            if "1 received" in output:
                print("Modem Nyala")
                break
            else:
                print("Modem Mati, mencoba lagi...")
        except subprocess.CalledProcessError:
            print("Modem Mati, mencoba lagi...")
        time.sleep(5)

if __name__ == "__main__":
    main()