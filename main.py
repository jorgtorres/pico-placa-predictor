#!/usr/bin/env python
import sys
from app.picoyplaca import PicoYPlaca as PP

def main():
    pp = PP('OBA-7970', '2017-08-04', '19:00')
    print("{0} Can be on the Road?: {1}".format(
        pp.getLicense(), "Yes" if pp.CanItBeOnRoad() else "No"))
    pp = PP('VFA-2134', '2017-11-07', '16:00')
    print("{0} Can be on the Road?: {1}".format(
        pp.getLicense(), "Yes" if pp.CanItBeOnRoad() else "No"))
    pp = PP('BBV-1235', '2017-11-08', '16:00')
    print("{0} Can be on the Road?: {1}".format(
        pp.getLicense(), "Yes" if pp.CanItBeOnRoad() else "No"))
    pp = PP('LOF-1540', '2017-08-11', '16:00')
    print("{0} Can be on the Road?: {1}".format(
        pp.getLicense(), "Yes" if pp.CanItBeOnRoad() else "No"))

if __name__ == '__main__':
    main()  