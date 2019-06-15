"""Pyrunc main package code"""

__author__ = "Kartikei Mittal"

# Python module(s)
import os
import subprocess
from ctypes import CDLL

COUNT = 0


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
        global COUNT
        with open("code.c", "w") as code_file:
            code_file.write(c_code)
        command = "gcc -w -shared -fPIC code.c -o shobj" + str(COUNT) + ".dll"
        a = subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout.decode(
            "utf-8"
        )
        shared_object = CDLL("shobj" + str(COUNT) + ".dll")
        COUNT += 1
        self.objs.append(shared_object)
        os.remove("code.c")
        return len(self.objs) - 1, shared_object
