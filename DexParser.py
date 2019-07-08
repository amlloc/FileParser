#!/usr/bin/env python3
#coding:utf-8
import binascii
import sys
from DexItem import DexHeader

class Dexfile:
    def __init__(self):
        super(Dexfile, self).__init__()
        print("init dexfile")
        # self.filePath = filePath
        self.DexHeader = DexHeader()
        self.init_header("/home/user/classes.dex")

    def init_header(self, filePath):
        f = open(filePath, "rb")
        self.DexHeader.file = f
        f.seek(0x0, 0)
        self.DexHeader.magic = binascii.b2a_hex(f.read(8))

def main():
    dex = Dexfile()


if __name__ == '__main__':
    main()






