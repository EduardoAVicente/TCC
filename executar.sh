#!/bin/bash

caminho="$(pwd)"

rm $caminho/bin/*

check_flags() {
    if [ "$1" = "-c" ]; then
        compilar
        exit
    elif [ "$1" = "-e" ]; then
        compilar
        java -classpath "$caminho/bin" Main
        exit
    elif [ -z "$1" ]; then
        compilar
        java -classpath "$caminho/bin" Main
        exit
    else
        echo "Flag não reconhecida: $1"
        echo "Use -e ou nenhum argumento para compilar e executar"
        echo "Use -c para compilar"
        exit 1
    fi
}

compilar() {
    if [ ! -d "$caminho/bin" ]; then
        mkdir "$caminho/bin"
    fi
    rm -f "$caminho/bin/*.*"
    javac -classpath "$caminho" -d "$caminho/bin" *.java
}

check_flags "$@"