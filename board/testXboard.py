#!/usr/bin/python

fd = open('/tmp/out', 'w+')

while(True):
  line = raw_input()
  fd.write(line + '\n')
  fd.flush()
  print 'Received:' , line
