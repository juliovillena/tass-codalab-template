#!/bin/bash
echo "Running test evaluation..."
python scoring_program/evaluate.py test/input test/output
echo "Done! Results are in test/output/scores.txt"
