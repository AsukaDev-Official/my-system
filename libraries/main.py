#!/usr/bin/env python3
#author : Tegar Dev
#komunitas : AsukaDev Official
#youtube : Asuka Dev
#name_file : main.py

import platform, colorama
exec(open("colors/.colors", "r").read())

class Main:
    def __init__(self):
        self.Info()
    def Info(self):
        my = platform.uname()
        print(f"[{kuning}{reset}] System : {hijau}{my.system}{reset}")
        print(f"[{kuning}{reset}] Node Name : {hijau}{my.node}{reset}")
        print(f"[{kuning}{reset}] Release : {hijau}{my.release}{reset}")
        print(f"[{kuning}{reset}] Version : {hijau}{my.version}{reset}")
        print(f"[{kuning}{reset}] Machine : {hijau}{my.machine}{reset}")
