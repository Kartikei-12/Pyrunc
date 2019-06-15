"""Pyrunc main package code"""

# Python module(s)
import os
import subprocess
from ctypes import CDLL


class Pyrunc:
    """Pyrunc package to embeed C code directly in python script"""

    def __init__(self, c_std="c11"):
        """init"""
        self.objs = list()
        self.c_std = c_std

    def build(self, c_code):
        """Build method building/compiling C code

        Args:
            c_code (str): Multiline C code to be compiled

        Returns:
            shared object: Shared object linking C code to python"""
        with open("code.c", "w") as code_file:
            code_file.write(c_code)
        command = "gcc -w -shared -fPIC code.c -o shobj" + str(len(self.objs)) + ".dll"
        a = subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout.decode(
            "utf-8"
        )
        shared_object = CDLL("shobj" + str(len(self.objs)) + ".dll")
        self.objs.append(shared_object)
        os.remove("code.c")
        return len(self.objs) - 1, shared_object
