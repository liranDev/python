import os
from xml.dom import minidom
import unittest
import multiprocessing
from unittest import TestLoader, TextTestRunner, TestSuite

tc_files = []
tc_root = 'TC.xml'

path = os.path.join(os.path.sep, os.path.dirname(__file__), tc_root)

with open(path, 'r') as xmldoc:

    xmldoc = minidom.parse(xmldoc)

    test_cases = xmldoc.getElementsByTagName('TestSuites')
    
    for tc in test_cases:

        for child in tc.getElementsByTagName('path'):

            tc_files.append(child.firstChild.nodeValue)
    

if __name__ == '__main__':

    for tc in tc_files:
        
        suite = unittest.TestLoader().loadTestsFromName(tc)

        multiprocessing.Process(target=unittest.TextTestRunner(verbosity=2).run(suite))
