#!/usr/bin/env python3

from concurrent.futures import process
from multiprocessing import Pipe
from pathlib import Path
from os import chdir, listdir, environ
from subprocess import PIPE, Popen
from sys import stderr, stdout, argv
import re

default_code_of = "diego"

folder = argv[1]
chdir(folder)

if len(argv) < 3: exec_code_of = default_code_of
else: exec_code_of = argv[2]

default_file = ""
if exec_code_of == "diego": default_file = "code.cpp"
elif exec_code_of == "gaton": default_file = f"gaton_{folder}.py"
else: raise NotImplementedError

if len(argv) < 4: exec_file = default_file
else: exec_file = argv[3] 

exec_file = Path(exec_file)

def compile(file: Path):
    process = Popen(['g++', '-std=c++11', '-O2', file], stderr=PIPE)
    _, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"can't compile {file}\n{stderr}")

def find_test_cases():
    for file in sorted(listdir('inputs')):
        if re.search(r'i\w*\d+\.txt', file): yield f'inputs/{file}'

exec_command = './a.out'
if exec_file.suffix == '.cpp':
    compile(exec_file)
elif exec_file.suffix == '.py':
    exec_command = f'python3 {exec_file}'

for test_case in find_test_cases():
    print(test_case)
    process = Popen(exec_command + f' < {test_case}', stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(stdout.decode('utf-8'))
        print("ERROR")
        print(stderr)
        print(f"codigo de error {process.returncode}")
        exit(0)
    else:
        number = re.findall(r'(\d+).txt', test_case)[0]
        print(f'outputs/o{number}.txt')
        with open(f'outputs/o{number}.txt', 'wb') as f:
            f.write(stdout)
        print(stdout.decode('utf-8'),end='---\n')
