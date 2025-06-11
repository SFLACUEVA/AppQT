#!/bin/bash
cd /home/sfl/Desktop/AppQT/
export DISPLAY=:0
/usr/bin/python3 /home/sfl/Desktop/AppQT/mainwindow.py &
echo $! > /tmp/inicio.pid