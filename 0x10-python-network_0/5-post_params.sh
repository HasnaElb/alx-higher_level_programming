#!/bin/bash
# send POST HTTP request with values for `email` and `subject` variables
curl -sX POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
