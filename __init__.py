#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
# Copyright © 2010 Andrew D. Yates
# All Rights Reserved.
"""unittest handle for Google App Engine Python.

Capture unittest stdout output and return it as a string. This string
can then be handled within an ordinary HTTP response. This is much
simpler and has less dependencies than other testing frameworks for
Python and App Engine.

Example:

>>> import sys
... import unittest
... import unittest_handle
... 
... class ExampleTest1(unittest.TestCase):
...   def test_example(self):
...     self.assertTrue(True)
... 
... class ExampleTest2(unittest.TestCase):
...   def test_example(self):
...     self.assertTrue(True)
... 
... def main(*args, **kwds):
...   out = unittest_handle.run(ExampleTest1, ExampleTest2)
...   print 'Content-Type: text/plain'
...   print ''
...   # avoid Python binary-to-ascii encoding errors in `print`
...   sys.stdout.write(test_output)
"""

import StringIO
import os
import unittest


def run(*argv):
  """Return the output from the execution of a list of TestCases.
  
  Args:
    *argv: [unittest.TestCase] list of test classes
    
  Returns:
    str: output from unittest execution of all test classes
  """
  out = StringIO.StringIO()
  for TestCase in argv:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(stream=out, verbosity=3).run(suite)
  return out.getvalue()
