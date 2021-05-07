#!/usr/bin/env python3
#author : Tegar Dev
#komunitas : AsukaDev Official
#youtube : Asuka Dev
#name_file : index.py

from libraries.main import *
import colorama

exec(open("colors/.colors", "r").read())
logo = lambda: print(f"\n{hijau} ___  _  _  ___  ____  ____  __  __\n/ __)( \/ )/ __)(_  _)( ___)(  \/  )\n\__ \ \  / \__ \  )(   )__)  )    (\n(___/ (__) (___/ (__) (____)(_/\/\_){reset}\n{bgwhite}        {abu}My System Information{reset}       {end}")

class Open:
    def __init__(self):
        self._Open()
    def _Open(self):
        try:
            Main()
        except:
            pass

if __name__=='__main__':
    logo()
    Open()

