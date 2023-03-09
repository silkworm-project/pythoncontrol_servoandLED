import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
io.setup(14, io.OUT)
io.setup(15, io.OUT)
io.setup(18, io.OUT)
io.setup(23, io.OUT)
io.setup(24, io.OUT)
io.setup(25, io.OUT)
io.setup(8, io.OUT)
io.setup(7, io.OUT)
io.setup(12, io.OUT)


io.output(14,1)
io.output(15,1)
io.output(18,0)
io.output(23,0)
io.output(24,0)
io.output(25,0)
io.output(8,0)
io.output(7,0)
io.output(12,0)

io.cleanup()
