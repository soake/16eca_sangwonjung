#-*- coding: utf8 -*-
# 2015110038 정상원

import root_finding

print dir(root_finding)

def func(x):
    return 1.0 * x * x - 3.0
print root_finding.sequential(func, 0.01)
