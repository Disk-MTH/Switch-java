@echo off
set /p setup_as=Setup as (user or system):

if exist "%~dp0..//python" (
	cd %~dp0..//python
	python.exe "%~dp0setup.py" %setup_as%
) else (
	python "%~dp0setup.py" %setup_as%
)