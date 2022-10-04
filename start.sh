#!/usr/bin/env bash

if [ $VIRTUAL_ENVIRONMENT ]
then 
    deactivate
fi
. familia_venv/Scripts/activate