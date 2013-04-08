# vim: set fileencoding=utf-8 :
"""This file should only be read when tests are running under python 3
if the pyramid.testing.NosePyVersion plugin is used"""
import sys

assert sys.version_info.major == 3

def test_version_matches():
    assert sys.version_info.major == 3
