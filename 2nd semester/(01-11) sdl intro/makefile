compiler = g++
libpath = ../../libs
libs = -lsdl2
output = ./bin
name = a.exe
source = ./src
objects = main.cpp

all: build

build:
	$(compiler) -g -o $(output)/$(name) $(source)/$(objects) -I$(libpath)/include -L $(libpath)/lib $(libs)
	
run: build
	$(output)/$(name)