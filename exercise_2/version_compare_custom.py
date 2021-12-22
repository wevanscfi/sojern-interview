#!/usr/bin/env python3
import sys
import re

def parse_version(v):
  return tuple(map(int, v.split(".")))

def main(v1, v2):
    v1 = parse_version(v1)
    v2 = parse_version(v2)

    if v1 > v2:
      sys.exit(1)
    if v2 > v1:
      sys.exit(-1)
    else:
      sys.exit(0)

if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])

