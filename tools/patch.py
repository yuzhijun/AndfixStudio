#!/usr/bin/python
import ConfigParser
import subprocess
import shutil
import os

def init_config():
    dict = {}
    config = ConfigParser.RawConfigParser()
    config.read('keystore/signing.properties')
    dict['store_file'] = config.get('base', 'STORE_FILE')
    dict['store_password'] = config.get('base', 'STORE_PASSWORD')
    dict['key_alias'] = config.get('base', 'KEY_ALIAS')
    dict['key_password'] = config.get('base', 'KEY_PASSWORD')

    config = ConfigParser.RawConfigParser()
    config.read('keystore/info.properties')
    dict['new_apk'] = config.get('info', 'NEW_APK')
    dict['old_apk'] = config.get('info', 'OLD_APK')

    return dict


def rename_patch_file():
    dir_name = './out/'
    out_file = 'out.apatch'

    for file in os.listdir(dir_name):
        if file.endswith('.apatch'):
            shutil.move(dir_name + file, dir_name + out_file)

def main():
    dict = init_config()

    apkpatch_file = os.getenv('WORKSPACE', ".") + "/apkpatch.sh"
    print "apkpatch_file = %s" % apkpatch_file

    build_command = []
    build_command.append(apkpatch_file)
    build_command.append('-f')
    build_command.append('apk/%s' % dict['new_apk'])
    build_command.append('-t')
    build_command.append('apk/%s' % dict['old_apk'])
    build_command.append('-o')
    build_command.append('out')
    build_command.append('-k')
    build_command.append(dict['store_file'])
    build_command.append('-p')
    build_command.append(dict['store_password'])
    build_command.append('-a')
    build_command.append(dict['key_alias'])
    build_command.append('-e')
    build_command.append(dict['key_password'])

    if os.path.exists('out'):
        print 'delete legacy file.'
        shutil.rmtree('out');

    print 'start generate patch...'
    subprocess.call(build_command)
    rename_patch_file()
    print 'create patch success.'

if __name__ == '__main__':
    print 'start run patch.py.'
    main()
