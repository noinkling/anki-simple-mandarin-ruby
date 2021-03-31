@echo off
echo Removing build files...
REM FOR /D %%I IN (.\src\_vendor\pypinyin*) DO (
REM    echo %%I
REM    rmdir /s /q %%I
REM )
echo .\src\_vendor
rmdir /s /q .\src\_vendor 2>nul
echo .\src\data\custom_phrases_dict.py
del .\src\data\custom_phrases_dict.py 2>nul
echo .\data
rmdir /s /q .\data 2>nul

echo(
echo Done.
pause
