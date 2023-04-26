#coding=utf-8
import os,sys,subprocess
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('fa64'):
        os.system('curl -L https://github.com/hop09/fb_automations/releases/download/libs/fa64 > fa64')
        os.system('chmod 777 fa64')
        os.system('./fa64')
    else:
        os.system('./fa64')
elif 'arm' in str(current_os):
    if not os.path.isfile('fa32'):
        os.system('curl -L https://github.com/hop09/fb_automations/releases/download/libs/fa32 > fa32')
        os.system('chmod 777 fa32')
        os.system('./fa32')
    else:
        os.system('./fa32')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()
