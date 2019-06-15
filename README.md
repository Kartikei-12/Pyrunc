# Pyrunc

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dc22a8634c3d48a3be630b7e7bba45c3)](https://www.codacy.com/app/Kartikei-12/Pyrunc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Kartikei-12/Pyrunc&amp;utm_campaign=Badge_Grade)
![Travis (.org)](https://img.shields.io/travis/Kartikei-12/Pyrunc.svg)
![Codecov](https://img.shields.io/codecov/c/github/Kartikei-12/Pyrunc.svg)
<hr>

## Introduction

A python package to directly embeed C/C++ code in python script/program/code.

## Project Description

*  Wrapper around `ctypes` Python package.
*  Tests in python 3.7 on Windows OS(by developer).
*  main.py contains simple metric for comparison.

## Installation

### Windows

    git clone https://github.com/Kartikei-12/Pyrunc
    cd Pyrunc-master
    python -m venv venv
    ./venv/Scripts/activate
    pip install -r requirements.txt

### Linux based OS

    git clone https://github.com/Kartikei-12/Pyrunc
    cd Pyrunc-master
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

## Usage

For simple example,

Run main.py as `python main.py` on **windows** with virtual environment(`./venv/Scripts/activate`).

Run main.py as `python3 main.py` on **Ubuntu/Linux** with virtual environment(`source /venv/Scripts/activate`).

## System Requirements

*  [Python 3](https://www.python.org/)
*  [Pip](https://pypi.org/) usually pre-installed with python, check with `pip3 --version`.
*  `GNU-GCC` is required to compile C code(working on packaging in project itself).

## Limitation

Currently only runs C code not C++ code as ctypes python module only supports C and not C++.

## Contributer(s)

[@Kartikei Mittal](https://github.com/Kartikei-12)





<!DOCTYPE html>
<html>

<body>
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <h2 class="text-capitalize">Unittest Results</h2>
                <p class='attribute'><strong>Start Time: </strong>2019-06-15 21:41:07</p>
                <p class='attribute'><strong>Duration: </strong>1.00 s</p>
                <p class='attribute'><strong>Summary: </strong>Total: 2, Pass: 2</p>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-md-10">
                <table class='table table-hover table-responsive'>
                    <thead>
                        <tr>
                            <th>__main__.DummyTests</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class='success'>
                            <td class="col-xs-10">test_dummy</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                Total: 1, Pass: 1 -- Duration: 0 ms
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-10 col-md-10">
                <table class='table table-hover table-responsive'>
                    <thead>
                        <tr>
                            <th>__main__.PyruncTests</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class='success'>
                            <td class="col-xs-10">test_simple_mathematical_formula</td>
                            <td class="col-xs-1">
                                <span class="label label-success" style="display:block;width:40px;">Pass</span>
                            </td>
                            <td class="col-xs-1">
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                Total: 1, Pass: 1 -- Duration: 1.00 s
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div></body></html>
