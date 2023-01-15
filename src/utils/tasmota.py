from json import loads as _loads
from requests import get as _get
from urllib.parse import quote as _parse
from setup.setup import TASMOTA_USER, TASMOTA_PASS


class TasmotaConstants:
    COMMAND_STATUS = "Status "
    COMMAND_NTP_SERVER = "NtpServer"
    COMMAND_UPGRADE = "Upgrade 1"
    STATUS_FIRMWARE = "StatusFWR"
    STATUS_NETWORK = "StatusNET"
    STATUS_MQTT = "StatusMQT"
    STATUS_TIME = "StatusTIM"
    VERSION = "Version"
    DNS_SERVER = "DNSServer"
    MQTT_USER = "MqttUser"
    MQTT_CLIENT = "MqttClient"
    MQTT_HOST = "MqttHost"
    MQTT_PORT = "MqttPort"
    TIME_LOCAL = 'Local'
    TIME_UTC = 'UTC'


def command(url_string, command):
    return _get(url_string + "/cm?cmnd=" + _parse(command), auth=(TASMOTA_USER, TASMOTA_PASS), timeout=2)


def backup(url_string):
    return _get(url_string + "/dl", auth=(TASMOTA_USER, TASMOTA_PASS), timeout=2)


def upgrade(url_string):
    return command(url_string, _parse(TasmotaConstants.COMMAND_UPGRADE))


def content(request):
    return _loads(request.content)
