from getpass import getpass
import os
import time
os.system('clear')
print('\x1b[1;31m[ Login ]')
print("")
print("")
print("")
x = raw_input('\x1b[1;33m[ Username/ID ]~> \x1b[1;36m')
print("")
e = getpass('\x1b[1;33m[ Password ]   ~> \x1b[1;36m')
print("")
if x=="3mweCyb3r56" and e=="emwe56":
   print('\x1b[1;33m[ Username Dan Password \x1b[1;32mBenar ]')
   time.sleep(3)
   os.system('python2 Tool.py')
else:
   print('\x1b[1;33m[ Username Dan Password\x1b[1;31m SALAH ]')
   print('\x1b[1;33m[ Silahkan Hubungi Author ]')
   os.system('xdg-open https://api.whatsapp.com/send?phone=6285956067789&text=Hai%20Author,%20saya%20ingin%20meminta%20Username%20dan%20Passwordnya%20terima%20kasih')
   time.sleep(10)
