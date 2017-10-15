#!/usr/bin/ruby

exp = open("/sys/class/gpio/export", "w")
exp.write(25)
exp.close

dir = open("/sys/class/gpio/gpio25/direction", "w")
dir.write("out")
dir.close

out = 1
5.times do
	  val = open("/sys/class/gpio/gpio25/value", "w")
	    val.write(out)
	      val.close
	        out = out == 1 ? 0 : 1
		  sleep 0.5
end

uexp = open("/sys/class/gpio/unexport", "w")
uexp.write(25)
uexp.close
