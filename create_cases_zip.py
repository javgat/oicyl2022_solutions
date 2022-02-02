#!/usr/bin/env python3
import os
import sys
import shutil

def main():
    destfolder = "temp"
    dirname = sys.argv[1]
    inputs = os.listdir(dirname+"/inputs")
    outputs = os.listdir(dirname+"/outputs")
    inputs.sort()
    outputs.sort()
    os.mkdir(destfolder+"/input")
    os.mkdir(destfolder+"/output")
    for i in range(len(inputs)):
        src = dirname+"/inputs/"+inputs[i]
        dst = destfolder+"/input/input"+"{:02d}".format(i)+".txt"
        shutil.copy2(src, dst)
    for i in range(len(outputs)):
        src = dirname+"/outputs/"+outputs[i]
        dst = destfolder+"/output/output"+"{:02d}".format(i)+".txt"
        shutil.copy2(src, dst)

if __name__ == "__main__":
    main()
