@echo off
set file=%WIN%m2.csv
py reader.py %file% 109
del var\%file%
time /t
