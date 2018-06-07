#!/usr/bin/env bash
which python3 &> /dev/null
if [[ $? -eq 0 ]];then
    PYTHON3BIN=`which python3`
    nohup $PYTHON3BIN manage.py runserver &> output.log
    [[ $? -eq 0 ]] && echo "start successful"
elif [[ -f /data/Android/new_script/test/python3/bin/python3 ]];then
    nohup /data/Android/new_script/test/python3/bin/python3 manager.py runserver &> output.log
    [[ $? -eq 0 ]] && echo "start successful"
else
    echo "no python3, quit now"
    exit 1
fi