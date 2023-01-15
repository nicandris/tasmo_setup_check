from re import findall
from utils.files import get_output_file
from utils.colors import print_status as ps, print_error as pe
from utils.tasmota import backup
from setup.urls import URLS as _URLS


def tasmotaBackup(url):
    try:
        response = backup(url)
        d = response.headers['content-disposition']
        file_name = findall("filename=(.+)", d)[0]

        with open(get_output_file(file_name), 'wb') as file:
            file.write(response.content)
        ps(url, file_name, response.status_code)
    except Exception as e:
        pe(e)


if __name__ == '__main__':
    for url in _URLS:
        tasmotaBackup(url)
        break
