@echo off
set tf=m5
if %d% == "" (
	py reader.py %t%%tf%.csv %*
) else (
	py reader.py %t%%tf%.csv %d% %*
	)
py ema.py 20 %t%%tf%.csv
time /t
