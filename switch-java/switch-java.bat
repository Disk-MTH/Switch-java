@echo off
if exist "%~dp0python" (
    echo Launch with bundled python
	cd %~dp0python
	python.exe "%~dp0switch-java.py"
) else (
    echo Launch with OS python
	python "%~dp0switch-java.py"
)