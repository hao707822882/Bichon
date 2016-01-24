#!/usr/bin/env python

# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
A clone of top / htop.

Author: Giampaolo Rodola' <g.rodola@gmail.com>

$ python examples/top.py
 CPU0  [|                                       ]   4.9%
 CPU1  [|||                                     ]   7.8%
 CPU2  [                                        ]   2.0%
 CPU3  [|||||                                   ]  13.9%
 Mem   [|||||||||||||||||||                     ]  49.8%  4920M/9888M
 Swap  [                                        ]   0.0%     0M/0M
 Processes: 287 (running=1 sleeping=286)
 Load average: 0.34 0.54 0.46  Uptime: 3 days, 10:16:37

PID    USER       NI  VIRT   RES   CPU% MEM%     TIME+  NAME
------------------------------------------------------------
989    giampaol    0   66M   12M    7.4  0.1   0:00.61  python
2083   root        0  506M  159M    6.5  1.6   0:29.26  Xorg
4503   giampaol    0  599M   25M    6.5  0.3   3:32.60  gnome-terminal
3868   giampaol    0  358M    8M    2.8  0.1  23:12.60  pulseaudio
3936   giampaol    0    1G  111M    2.8  1.1  33:41.67  compiz
4401   giampaol    0  536M  141M    2.8  1.4  35:42.73  skype
4047   giampaol    0  743M   76M    1.8  0.8  42:03.33  unity-panel-service
13155  giampaol    0    1G  280M    1.8  2.8  41:57.34  chrome
10     root        0    0B    0B    0.9  0.0   4:01.81  rcu_sched
339    giampaol    0    1G  113M    0.9  1.1   8:15.73  chrome
...
"""

from datetime import datetime
from datetime import timedelta
import atexit
import os
import sys
import time


import psutil


lineno = 0




def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return "%sB" % n


# def poll(interval):
    # sleep some time


    # # return processes sorted by CPU percent usage
    # processes = sorted(procs, key=lambda p: p.dict['cpu_percent'],
    #                    reverse=True)
    # return processes


def print_header(procs_status, num_procs):
    """Print system-related info, above the process list."""






def refresh_window(procs):
    """Print results on screen by using curses."""

    print "---------------------------------------"
        #for p in procs:
        # TIME+ column shows process CPU cumulative time and it
        # is expressed as: "mm:ss.ms"

        #print p.dict['cpu_percent']


def main():
    try:
        interval = 1


        for p in psutil.process_iter():
            try:
                p.dict = p.as_dict(['username', 'nice', 'memory_info',
                                    'memory_percent', 'cpu_percent',
                                    'cpu_times', 'name', 'status'])
                print p.dict["cpu_percent"]
            except psutil.NoSuchProcess:
                pass
        print "----------------------------------"
        time.sleep(interval)
        for p in psutil.process_iter():
            try:
                p.dict = p.as_dict(['username', 'nice', 'memory_info',
                                    'memory_percent', 'cpu_percent',
                                    'cpu_times', 'name', 'status'])
                print p.dict["cpu_percent"]
            except psutil.NoSuchProcess:
                pass
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    main()