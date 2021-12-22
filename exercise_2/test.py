#!/usr/bin/env python3

import version_compare
import version_compare_custom

def test_version_compare(v1, v2):
  print("Comparing %s to %s returns" %(v1, v2))

  print(version_compare.main(v1, v2))

def test_version_compare_custom(v1, v2):
  print("Comparing %s to %s returns" %(v1, v2))

  print(version_compare_custom.main(v1, v2))

if __name__ == "__main__":
  print("Testing version_compare")
  test_version_compare("1.2.3", "2.34.5")
  test_version_compare("v1.2.3", "2.34.5")
  test_version_compare("1.2.3rc", "2.34.5")
  test_version_compare("2.5", "2.34.5")
  test_version_compare("7.2.3", "2.34")
  test_version_compare("7.2.3", "v7.2.3")

  print("Testing version_compare_custom")
  test_version_compare_custom("1.2.3", "2.34.5")
  test_version_compare_custom("2.5", "2.34.5")
  test_version_compare_custom("7.2.3", "2.34")
  test_version_compare_custom("7.2.3", "7.2.3")
