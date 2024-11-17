from oct2py import Oct2Py, get_log
import numpy as np
import scipy.signal as signal
import scipy.io
import logging


oc = Oct2Py(logger=get_log())

oc.logger = get_log('new_log')
oc.logger.setLevel(logging.INFO)


oc.eval("pkg load control")
oc.eval("pkg load signal")
oc.eval("pkg load statistics")

result = oc.eval("openibis()")

print(result)

print(type(result))
a = result.transpose()

# x = oc.zeros(1,3)

# print(x)