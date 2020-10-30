#!/bin/bash
/usr/bin/python3 /home/sanjay/1Stocks/Stock_predictor/command.py -pv y & TASK1_PID=$!
while ps -p $TASK1_PID; do sleep 1; done;