import os
import subprocess
from ctypes import CDLL


class Pyrunc:
    def __init__(self, cplusplus_std="c++14"):
        self.objs = list()
        self.cplusplus_std = cplusplus_std

    def build(self, c_cpp_code):
        with open("code.cpp", "w") as code_file:
            code_file.write(c_cpp_code)
        # -std='+self.gplusplus_std+'  -lstdc++ -std=c++11
        command = "gcc -w -shared -fPIC code.cpp -o shobj.dll"
        a = subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout.decode(
            "utf-8"
        )
        shared_object = CDLL("shobj.dll")
        self.objs.append(shared_object)
        # print([ m for m in dir(shared_object) if not m.startswith('__')])
        os.remove("code.cpp")
        # os.remove('shobj.dll')
        return len(self.objs) - 1, shared_object
