#!/bin/bash


#n=$(grep -E -o "0.0.[0-9]+" setup1.py | cut -d "." -f 3)
#echo $n
#next=$((n+1))
#echo $next

rm ./dist/*
python setup.py sdist bdist_wheel
twine upload dist/* --verbose
