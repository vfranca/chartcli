@echo off
set file=win@daily.csv
py reader.py %file% %*
rem del var\%file%
time /t
