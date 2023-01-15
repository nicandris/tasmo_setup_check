from setup.urls import URLS as _URLS
from utils.colors import print_status as ps, print_error as pe
from utils.tasmota import upgrade


def tasmotaUpgrade(url):
    try:
        ps(url, 'Upgrading...', upgrade(url).status_code)
    except Exception as e:
        pe(e)


if __name__ == '__main__':
    for url in _URLS:
        tasmotaUpgrade(url)
        break
