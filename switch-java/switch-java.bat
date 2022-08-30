@echo off
set /p java_version=The java version to set: 

if exist "%~dp0python" (
	cd %~dp0python
	python.exe "%~dp0switch-java.py" %java_version%
) else (
	python "%~dp0switch-java.py" %java_version%
)