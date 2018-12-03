#!/bin/bash
if [ ! -d "$1" ]; then
  echo "Creating directory for day: $1"
  mkdir $1
  echo "Touching input-files"
  touch $1/input.txt
  touch $1/test.txt
  echo "Copying template"
  cp template.py $1/solve.py
  echo "Done!"
else
  echo "Day $1 already exists, aborting!"
fi