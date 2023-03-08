import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
io.setup (21, io.OUT)

io.output(21,1)
sleep(5)

io.output(21,0)
io.cleanup()