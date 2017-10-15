#!/usr/bin/ruby

require 'pi_piper'
include PiPiper

pin = Pin.new pin:25, direction: :out

5.times do
	pin.on
	sleep 0.5
	pin.off
	sleep 0.5
end

uexp = open("/sys/class/gpio/unexport", "w")
uexp.write(25)
uexp.close
