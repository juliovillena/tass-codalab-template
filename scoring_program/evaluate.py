#!/usr/bin/env python
import sys
import os
import os.path

input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if not os.path.isdir(submit_dir):
  print "%s doesn't exist" % submit_dir

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  output_filename = os.path.join(output_dir, 'scores.txt')
  output_file = open(output_filename, 'wb')

  truth_file = os.path.join(truth_dir, "truth.txt")
  truth = [x.strip() for x in open(truth_file).readlines()] 

  answer_file = os.path.join(submit_dir, "answer.txt")
  answer = [x.strip() for x in open(answer_file).readlines()] 

  accuracy = 0

  if len(truth)!=len(answer):
    print "Expected %d lines but read just %d lines" % (len(truth), len(answer))
  else:
    ok = 0
    err = 0
    for x in zip(truth, answer):
      if x[0]==x[1]:
        ok += 1
      else:
        err += 1
    accuracy = 1.0*ok/(ok+err)

  output_file.write("accuracy: %0.3f\n" % accuracy)

output_file.close()
