#!/bin/bash
RAN=`echo $(($RANDOM % 10))`
LOG="~/mikke/log/h1.log"
WAV1="~/mikke/wav/p2.wav trim ${RAN} 1.5 phaser 0.6 0.66 3 0.6 2 -t bass -30 reverb"
WAV2="-n synth 0.1 saw 100-200 sine 440-100"
WAV3="-n synth 0.1 pinknoise 100 sine 240-90"

RP=3

echo $(($RANDOM % RP))

if [ $(($RANDOM % 3)) = 0 ]; then
	echo "test1"
	play ${WAV1}
elif [ $(($RANDOM % 3)) = 1 ]; then
	echo "test2"
	play ${WAV2}
elif [ $(($RANDOM % 3)) = 2 ]; then
	echo "test3"
	play ${WAV3}
fi
