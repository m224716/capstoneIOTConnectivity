#!/usr/bin/env python3
from doctest import master
from Alexa import *
from GA import *
from RingDB import *
from gashm import *
import sys
import json
import os

def StartingPoint():
    device = input("What Device are you accessing?\n Alexa\n Google Home\n Ring Doorbell\n Nest Doorbell\n Google Assistant\n")
    print("Starting API for" + device + "..." )
    if device == "Google Home" or device == "google home":
        print('hi')
        os.chdir('\Users\m225124\Downloads\CapstoneCode\gashm')
        GHomeAPI()
    if "ring" or "Ring" in device:
        print('hi')
        RingAPI()
    if "eufy" or "Eufy" in device:
        print('i')
        eufyAPI()
    else:
        print("Sorry didn't catch that")
        StartingPoint()

def GHomeAPI():
    os.chdir('\Users\m225124\Downloads\CapstoneCode\gashm')
    uname = input("Enter your username")
    pword = input("Enter your password")
    print('hi')

def RingAPI():
    os.chdir('\Users\m225124\Downloads\CapstoneCode\PythonRingDB')
    uname = input("Enter your username")
    pword = input("Enter your password")
    print("hi")

def eufyAPI():
    os.chdir('\Users\m225124\Downloads\CapstoneCode\eufyDB')
    uname = input("Enter your username")
    pword = input("Enter your password")
    print("hi")