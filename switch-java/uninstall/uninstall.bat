@echo off
if exist "%~dp0..//python" (
    echo Launch with bundled python
	cd %~dp0..//python
	python.exe "%~dp0uninstall.py"
) else (
    echo Launch with OS python
	python "%~dp0uninstall.py"
)