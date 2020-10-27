#!/bin/bash
/usr/bin/python3 /home/sanjay/1Stocks/Stock_predictor/command.py -sl y & TASK1_PID=$!
while ps -p $TASK1_PID; do sleep 60; done;

/usr/bin/python3 /home/sanjay/1Stocks/Stock_predictor/command.py -pgw y & TASK1_PID=$!
while ps -p $TASK1_PID; do sleep 1; done;