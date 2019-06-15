# Pyrunc

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)<hr>

## Introduction

A python package to directly embeed C/C++ code in python script/program/code.

## Project Description

*  Wrapper around `ctypes` Python package.
*  Tests in python 3.7 on Windows OS(by developer).
*  main.py contains simple metric for comparison

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
                <p class='attribute'><strong>Start Time: </strong>2019-06-15 21:08:20</p>
                <p class='attribute'><strong>Duration: </strong>1.55 s</p>
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
                                Total: 1, Pass: 1 -- Duration: 1.55 s
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div></body></html>
