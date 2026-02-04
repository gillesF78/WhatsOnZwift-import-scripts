#!/usr/bin/env python
# -*- coding: utf-8; fill-column: 120; truncate-lines: t -*-
# from https://forum.intervals.icu/t/workout-builder/1163/423
# see also https://cubingtest.byethost9.com/Other/CyclingCalculator.html
# Usage : text-to-whatsonzwift.icu.py "Dirty Teeth Drills.txt"

import re
import sys

def convert(zwift):
    icu = ""
    multiplier = False

    # expand multiplied lines
    for line in zwift:
        if re.match('^[1-9]+[xX] .*,\\s*\\Z', line):
            icu += '\n' + line[:3] + '\n'
            icu += '- ' + line[3:]
            multiplier = True
        elif re.match('^[1-9]+[xX]', line):
            icu += '\n' + line[:3] + '\n'
            icu += '- ' + line[3:]
            multiplier = False
        elif multiplier == True:
            icu += '- ' + line + '\n'
            multiplier = False
        else:
            icu += '- ' + line

    # replace words and fix grammar
    icu = icu.replace('min', 'm').replace('sec', 's') \
            .replace('from', 'ramp').replace(' to ', '-') \
            .replace('FTP', '').replace(',', '').replace('@', '').replace('\n+', '\n') + '\n'
    icu = re.sub('([0-9]+m) ([0-9]+s)', '\\1\\2', icu)

    return icu



if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as zwift:
        print(convert(zwift))

