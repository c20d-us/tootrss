#!/bin/bash

PY=`/usr/bin/which python3`

${PY} -m venv venv

. venv/bin/activate

pip install --upgrade pip

pip install wheel

pip install -r ./requirements.txt

deactivate
