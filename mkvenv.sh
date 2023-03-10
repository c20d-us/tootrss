#!/bin/bash

PY3=`/usr/bin/which python3`
REQS="./requirements/reqs.txt"

function quit_error {
	printf "\n${1} ... exiting.\n\n"
	exit 1
}

/usr/bin/clear

[ -x "${PY3}" ] || quit_error "You do not appear to have a usable python3 available on your system"

printf "\nMaking the venv folder ... "
${PY3} -m venv venv > /dev/null 2>&1 || quit_error "There was an error making the venv"
printf "done\n"

printf "\nActivating the environment ... "
source venv/bin/activate || quit_error "There was an error activating the venv"
printf "done\n"

printf "\nInstalling requirements ...\n"
pip install -q --upgrade pip > /dev/null 2>&1 && \
  pip install -q wheel > /dev/null 2>&1 && \
  pip install -q -r "${REQS}" > /dev/null 2>&1 || quit_error "There was an error installing the requirements"

printf "\nmkvenv is complete!\n"

deactivate
