@echo off

SET SCRIPT_NAME=python-vendorize

FOR %%I IN (%SCRIPT_NAME%) DO (SET SCRIPT_PATH=%%~$PATH:I)

IF DEFINED SCRIPT_PATH (
    echo py %SCRIPT_PATH%
    py %SCRIPT_PATH%
) ELSE (
    echo Couldn't find %SCRIPT_NAME%
    echo Run `py -m pip install -r requirements-dev.txt`
    echo or activate your virtual environment if you forgot to.
)

echo(
pause
