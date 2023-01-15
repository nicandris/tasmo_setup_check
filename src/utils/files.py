from os import path as _path

BACKUP_FOLDER = '../../Backups'


def get_output_file(filename):
    return _path.join(_path.dirname(__file__), BACKUP_FOLDER, filename)
