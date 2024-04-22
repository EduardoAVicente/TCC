@echo off
cls


for %%I in ("%CD%") do (
    set "caminho=%%~I"
)

:CheckFlags
if "%~1"=="-c" (
    call :compilar
    goto :eof
) else if "%~1"=="-e" (
    call :compilar
    java -classpath "%caminho%\bin" Main
    goto :eof
) else if "%~1"=="" (
    call :compilar
    java -classpath "%caminho%\bin" Main
    goto :eof
) else (
    echo Flag nao reconhecida: %1
    echo Use -e ou nenhum argumento para compilar e executar
    echo Use -c para compilar
    goto :eof
)

:compilar

if not exist "%caminho%\bin" (
    mkdir "%caminho%\bin"
)
del /Q "%caminho%\bin\*.*"
cls
javac -classpath "%caminho%" -d "%caminho%\bin" *.java
goto :eof