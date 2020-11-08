import os
import sys
import time

time.sleep(1)
os.system ('clear')
print ('\x1b[1;34m')
os.system ('figlet Tools')
print('\x1b[1;33m=================================')
print('\x1b[1;36m Author : 3mweCyb3r56 ')
print('\x1b[1;36m Team   : IndCyX-Termux ')
print('\x1b[1;33m=================================')
print('\x1b[1;35m++++++++++++ \x1b[1;36mM E N U \x1b[1;35m++++++++++++')
print('\x1b[1;34m[1] \x1b[1;36mBrutalSpammer           \x1b[1;32m[Work]')
print('\x1b[1;34m[2] \x1b[1;36mSeeker                 \x1b[1;31m[Broken]')
print('\x1b[1;34m[3] \x1b[1;36mPhising-Game-Installer  \x1b[1;32m[Work]')
print('\x1b[1;34m[4] \x1b[1;36mTerkey                  \x1b[1;32m[Work]')
print('\x1b[1;34m[5] \x1b[1;36mSayCheese              \x1b[1;31m[Broken]')
print('\x1b[1;35m[0] \x1b[1;37mExit ')
gans = raw_input ('\x1b[1;36m[ Pilih Nomor ]>>> ')
if gans in ['1']:
    time.sleep(1)
    os.system ('git clone https://github.com/IL4NGQW3R/brutalspammer')
    print ('\x1b[1;33mlanjut ketikan cd brutalspammer')
    print ('\x1b[1;33mlalu python BrutalSpammer.py')
    exit()
if gans in ['2']:
    time.sleep(1)
    os.system ('git clone https://github.com/thewhiteh4t/seeker')
    print ('\x1b[1;33mlanjut ketikan cd seeker')
    print ('\x1b[1;33mlalu chmod 777 termux_install.sh')
    print ('\x1b[1;33msetelah itu bash termux_install.sh')
    print ('\x1b[1;33mterakhir python seeker.py -t manual -k kmltest')
    exit()
if gans in ['3']:
    time.sleep(1)
    os.system ('git clone https://github.com/Cyser-Inc/Phising-Game-Online')
    print ('\x1b[1;33mlanjut ketikan cd Phising-Game-Online')
    print ('\x1b[1;33mlalu python2 phising.py')
    exit()
if gans in ['4']:
    time.sleep(1)
    os.system ('git clone https://github.com/karjok/terkey')
    print ('\x1b[1;33mlanjut ketikan cd terkey')
    print ('\x1b[1;33mlalu python terkey.py')
    exit()
if gans in ['5']:
    time.sleep(1)
    os.system('git clone https://github.com/Anonymous3-SIT/saycheese')
    print ('\x1b[1;33mlanjut ketikan cd saycheese')
    print ('\x1b[1;33mlalu chmod +x *')
    print ('\x1b[1;33mterakhir bash saycheese.sh')
    exit()
if gans in ['0']:
    time.sleep(2)
    exit()
else:
    time.sleep(1)
    print '\x1b[1;32mPilih Yang Bener '
    time.sleep(1)
