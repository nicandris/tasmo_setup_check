from setup.urls import URLS as _URLS
from setup.setup import SERVER_IP, PIHOLE_IP
from utils.colors import print_status as ps, print_error as pe
from utils.tasmota import command


# Commands
CHANGE_TIMEZONE = "Backlog0 Timezone 99; TimeStd 0,0,10,1,3,60; TimeDst 0,0,3,1,2,120"
NTP_SERVER = "NtpServer1 {}".format(SERVER_IP)
DNS_SERVER = "IPAddress4 {}".format(PIHOLE_IP)

COMMAND = NTP_SERVER


def change(url):
    try:
        ps(url, COMMAND, command(url, COMMAND).status_code)
    except Exception as e:
        pe(e)


if __name__ == '__main__':
    for url in _URLS:
        change(url)
        #break
