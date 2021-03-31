@echo off
setlocal

REM Stops __pycache__ folders / .pyc files being generated on import.
SET PYTHONDONTWRITEBYTECODE=1

echo Vendorizing dependencies...
echo vendorize.cmd
echo(
call vendorize.cmd && (
echo(
echo Downloading ^(better^) pinyin dictionary and converting it...
echo fetch_data.cmd
echo on
call fetch_data.cmd
) && (
@echo off
echo(
echo Done.
)
pause
