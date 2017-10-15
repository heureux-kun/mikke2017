#!/usr/bin/ruby

require "pi_piper"
include PiPiper

pin = Pin.new pin:25, direction: :out

pin.off

uexp = open("/sys/class/gpio/unexport", "w")
uexp.write(25)
uexp.close
