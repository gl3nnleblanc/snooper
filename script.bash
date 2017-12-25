#!/bin/bash
cat tcpdumpoutput | sed 's/ IP /,/g' | sed 's/ > /,/g' | sed 's/: .*//g' | python3 snooper.py
