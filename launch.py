#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
TF_Curses
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
./launch.py

 * this should provide a non installed working clent
"""
import sys
import dummy.os.__main__ as app

if __name__ == '__main__':
    try:
        app.main(sys.argv)
    except Exception as e:
        print("Thanks for using Alphagriffin.com\nExit Error:\n{}".format(e))
