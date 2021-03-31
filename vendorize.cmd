@echo off
setlocal

REM The version of Python that our lowest supported version of Anki uses:
SET PIP_PYTHON_VERSION=3.8

REM Use non-binary version of packages (if there is a choice), since Anki supports multiple platforms:
REM SET PIP_NO_BINARY=:all:

REM Use a platform-agnostic "wheel" (distribution archive) if one exists, since Anki
REM supports multiple platforms. This usually means that the package is pure Python.
REM Will fall back to source distribution otherwise (if available), in which case it
REM probably won't work cross-platform.
SET PIP_PLATFORM=any
REM SET PIP_ABI=none

REM Stops __pycache__ folders / .pyc files being generated on install.
REM For some reason this environment variable needs to be set to 0 to activate the option...
REM See: https://pip.pypa.io/en/stable/user_guide/#config-file
SET PIP_NO_COMPILE=0

SET SCRIPT_NAME=python-vendorize

FOR %%I IN (%SCRIPT_NAME%) DO (SET SCRIPT_PATH=%%~$PATH:I)

IF DEFINED SCRIPT_PATH (
    echo py %SCRIPT_PATH% ^&^& rmdir /s /q .\src\_vendor\bin
    py %SCRIPT_PATH% && rmdir /s /q .\src\_vendor\bin
) ELSE (
    echo Couldn't find %SCRIPT_NAME%
    echo Run `py -m pip install -r requirements-dev.txt`
    echo or activate your virtual environment if you forgot to.
)
