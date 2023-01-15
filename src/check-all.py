import setup.setup as check
from utils.date import compare_dates, convert_string
from utils.colors import print_result as pr, print_error as pe, print_title as pt
from utils.tasmota import TasmotaConstants as tconst
from utils.tasmota import command, content
from setup.urls import URLS as _URLS


def checkVersion(url):
    response = command(url, tconst.COMMAND_STATUS + '2')
    version = content(response)[tconst.STATUS_FIRMWARE][tconst.VERSION]

    pr(version.startswith(check.CHECK_VERSION),
       "{}: {}".format(tconst.VERSION, version))


def checkNtp(url):
    response = command(url, tconst.COMMAND_NTP_SERVER)
    ntp = content(response)[tconst.COMMAND_NTP_SERVER + '1']

    pr(check.CHECK_NTP == ntp, "{}: {}".format(tconst.COMMAND_NTP_SERVER, ntp))


def checkDNS(url):
    response = command(url, tconst.COMMAND_STATUS + '5')
    rcontent = content(response)[tconst.STATUS_NETWORK]
    dns = rcontent[tconst.DNS_SERVER + '1']
    dns2 = rcontent[tconst.DNS_SERVER + '2']

    pr(check.CHECK_DNS == dns or check.CHECK_DNS == dns2,
       "DNS Server: {} / {}".format(dns, dns2))


def checkMQTT(url):
    response = command(url, tconst.COMMAND_STATUS + '6')
    rcontent = content(response)[tconst.STATUS_MQTT]
    mqttUser = rcontent[tconst.MQTT_USER]
    mqttClient = rcontent[tconst.MQTT_CLIENT]
    mqttHost = rcontent[tconst.MQTT_HOST]
    mqttPort = rcontent[tconst.MQTT_PORT]

    pr((check.CHECK_MQTT_HOST == mqttHost) and (check.CHECK_MQTT_PORT == str(mqttPort)) and (
        mqttUser in url) and (mqttClient in url), 'MQTT: {} - {}:{}'.format(mqttUser, mqttHost, mqttPort))


def checkTime(url):
    response = command(url, tconst.COMMAND_STATUS + '7')
    rcontent = content(response)[tconst.STATUS_TIME]
    localTime = rcontent[tconst.TIME_LOCAL]
    utcTime = rcontent[tconst.TIME_UTC]

    pr(compare_dates(localTime), 'Time: ' + '{}: {} - {}: {}'.format(tconst.TIME_LOCAL,
       convert_string(localTime), tconst.TIME_UTC, convert_string(utcTime)))


if __name__ == '__main__':
    for url in _URLS:
        try:
            print('')
            pt(url)
            checkVersion(url)
            checkMQTT(url)
            checkDNS(url)
            checkNtp(url)
            checkTime(url)
        except Exception as e:
            pe(e)
        #break
