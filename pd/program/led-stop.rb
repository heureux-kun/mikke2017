#!/usr/bin/ruby

exp = open("/sys/class/gpio/export", "w")
exp.write(27)
exp.close

dir = open("/sys/class/gpio/gpio27/direction", "w")
dir.write("out")
dir.close

uexp = open("/sys/class/gpio/unexport", "w")
uexp.write(27)
uexp.close
