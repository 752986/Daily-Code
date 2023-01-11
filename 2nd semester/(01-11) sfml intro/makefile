compiler = g++
sfml = C:/Users/752986/Documents/cpplib/SFML-2.5.1
libs = -lsfml-graphics -lsfml-window -lsfml-system
output = ./bin
name = a.exe
source = ./src
objects = main.cpp

all: build

build:
	$(compiler) -static -g -o $(output)/$(name) $(source)/$(objects) -I $(sfml)/include -L $(sfml)/lib $(libs)
	
run: build
	$(output)/$(name)