# vim: set fileencoding=utf-8 :
"""This file should only be read when tests are running under python 2
if the pyramid.testing.NosePyVersion plugin is used"""
import sys

assert sys.version_info.major == 2

def test_version_matches():
    """Test that python major version is 2"""
    assert sys.version_info.major == 2
